"""Generate a bounded, closed-surface passive rocket external-flow pilot case.

This is a pilot, not accepted CFD evidence. No flight coefficient override is made.
"""
import argparse
import math
import struct
import hashlib
from collections import Counter
from pathlib import Path

import cadquery as cq
import numpy as np
from rocket_workbench.cli import save_json
from rocket_workbench.config import load_config, mass_cg
from rocket_workbench.cad import shapes


def foam(path, body, cls='dictionary'):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text('FoamFile { version 2.0; format ascii; class '+cls+'; object '+path.name+'; }\n'+body+'\n')


def surface_mesh(solid, path):
    """Remove zero-area apex facets, then require a closed two-manifold triangle mesh."""
    from OCP.BRepMesh import BRepMesh_IncrementalMesh
    from OCP.BRepTools import BRepTools
    # CadQuery's default mesher uses relative deflection. At the thin leading
    # root/collar junction that produced incompatible adjacent-face triangulations.
    # Use explicit absolute deflection in metres and discard cached meshes.
    BRepTools.Clean_s(solid.wrapped)
    BRepMesh_IncrementalMesh(solid.wrapped, 1e-5, False, .05, False)
    vertices,triangles=solid.tessellate(.00005,.05)
    vertices=[tuple(round(v,9) for v in point.toTuple()) for point in vertices]
    faces=[]
    edges=Counter()
    seen=set()
    removed=0
    for indices in triangles:
        points=[vertices[i] for i in indices]
        normal=np.cross(np.subtract(points[1],points[0]),np.subtract(points[2],points[0]))
        norm=float(np.linalg.norm(normal))
        key=tuple(sorted(points))
        if norm<=1e-18 or key in seen:
            removed+=1
            continue
        seen.add(key)
        faces.append((normal/norm,points))
        for a,b in zip(points,points[1:]+points[:1]):
            edges[tuple(sorted((a,b)))]+=1
    if not faces or set(edges.values())!={2}:
        bad=[(edge,count) for edge,count in edges.items() if count != 2]
        raise ValueError('CFD triangulation is not closed two-manifold after degenerate-facet removal: '
                         f'{len(bad)} bad edges; incidence counts {dict(Counter(c for _,c in bad))}; '
                         f'examples {bad[:3]}')
    header=b'Rocket workbench CFD exterior; metres'.ljust(80,b' ')
    data=bytearray(header+struct.pack('<I',len(faces)))
    for normal,points in faces:
        data.extend(struct.pack('<12fH',*normal,*(v for p in points for v in p),0))
    path.write_bytes(data)
    return dict(triangles=len(faces),removed_degenerate_or_duplicate=removed,weld_precision_m=1e-9,
                absolute_deflection_m=1e-5,angular_deflection_rad=.05,relative_deflection=False)


def generate(config, out, cell_mm=40, speed=40, alpha=0, iterations=600, ring_chord_mm=0):
    if ring_chord_mm not in (0, 5, 10):
        raise ValueError('Ring comparison supports only the retained 0/5/10 mm chord trials')
    out.mkdir(parents=True,exist_ok=False)
    save_json(out/'resolved-inputs.json',config.model_dump())
    g=config.geometry
    n,r,length=g.mm('nose_length'),g.mm('body_od')/2,g.mm('body_length')
    if config.nose_shape!='conical':
        raise ValueError('Pilot external surface currently supports conical nose only')
    # Filled exterior, no internal printing cavities or unsealed artificial flow paths.
    nose=cq.Workplane(obj=cq.Solid.makeCone(0,r,n))
    body=cq.Workplane('XY',origin=(0,0,n)).circle(r).extrude(length)
    start=n+length-g.mm('collar_length')
    radius=r+g.mm('clearance')+g.mm('wall')
    fill=cq.Workplane('XY',origin=(0,0,start)).circle(radius).extrude(g.mm('collar_length'))
    fairing=cq.Workplane(obj=cq.Solid.makeCone(r,radius,g.mm('fairing_length'),cq.Vector(0,0,start-g.mm('fairing_length'))))
    parts=shapes(config)
    _,dry_cg=mass_cg([(p.val().Volume()*config.density.value/1000,p.val().Center().z) for p in parts.values()]
        +[(p.mass.value,p.x.value) for p in config.purchased_masses]
        +[(config.payload.mass.value,config.payload.cg_x.value)])
    added_ring_mass=0.
    if ring_chord_mm:
        from rocket_workbench.nonplanar import ring_tail
        original=parts['fin-collar']
        parts['fin-collar']=ring_tail(config,original,chord_mm=ring_chord_mm)
        added_ring_mass=(parts['fin-collar'].val().Volume()-original.val().Volume())*config.density.value/1000
    external=nose.union(body).union(fill).union(fairing).union(parts['fin-collar'])
    if not external.val().isValid() or len(external.solids().vals())!=1:
        raise ValueError('External flow geometry must be one closed valid solid')
    # Round-trip the actual external STEP to avoid stale per-face triangulations
    # inherited from CAD mass/boolean operations. Closure remains a hard gate.
    cq.exporters.export(external,str(out/'external-mm.step'))
    external=cq.importers.importStep(str(out/'external-mm.step'))
    solid=external.val().rotate((0,0,0),(0,1,0),90).scale(.001)
    surface=out/'constant/triSurface/rocket.stl'
    surface.parent.mkdir(parents=True)
    mesh=surface_mesh(solid,surface)
    angle=math.radians(alpha)
    ux,uy=speed*math.cos(angle),speed*math.sin(angle)
    velocity=f'({ux:.10g} {uy:.10g} 0)'
    k=1.5*(.01*speed)**2
    omega=math.sqrt(k)/(.09**.25*.004)
    refarea=math.pi*(r*.001)**2
    save_json(out/'case-spec.json',dict(design=config.name,cell_mm=cell_mm,speed_m_s=speed,alpha_deg=alpha,
        iterations=iterations,reference_area_m2=refarea,reference_length_m=2*r*.001,
        moment_origin_m=[dry_cg*.001,0,0],
        ring_tail=dict(chord_mm=ring_chord_mm,wall_mm=1.2 if ring_chord_mm else None,
                       added_cad_mass_g=added_ring_mass,
                       force_reference='Unmodified planar baseline dry CG retained for matched moment comparison',
                       flight_model_updated=False),
        axes='x nose to aft; flow +x; positive alpha adds +y flow; v2512 drag/lift basis reports pitch about -z; verify output headers',
        limitations=['Pilot only; no launch lugs, nozzle cavity, exhaust plume, surface roughness or flexibility',
                    'Moment origin is planar-baseline loaded dry CG; ring and instantaneous motor mass need a reference shift for flight use',
                    'Fully turbulent incompressible kOmegaSST; transition and compressibility not assessed',
                    'No boundary layers in pilot mesh; do not accept drag ranking before wall/mesh checks'],
        mesh=mesh,generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        accepted_for_design=False))
    nx,ny=math.ceil(2.5/(cell_mm*.001)),math.ceil(.8/(cell_mm*.001))
    foam(out/'system/blockMeshDict',f'''convertToMeters 1;
vertices ((-.5 -.4 -.4) (2 -.4 -.4) (2 .4 -.4) (-.5 .4 -.4)
          (-.5 -.4 .4) (2 -.4 .4) (2 .4 .4) (-.5 .4 .4));
blocks (hex (0 1 2 3 4 5 6 7) ({nx} {ny} {ny}) simpleGrading (1 1 1));
edges ();
boundary (
 inlet {{type patch; faces ((0 4 7 3));}}
 outlet {{type patch; faces ((1 2 6 5));}}
 farfield {{type patch; faces ((0 1 5 4) (3 7 6 2) (0 3 2 1) (4 5 6 7));}}
);
mergePatchPairs ();''')
    foam(out/'system/snappyHexMeshDict','''castellatedMesh true; snap true; addLayers false;
geometry { rocket.stl {type triSurfaceMesh; name rocket;}
 wake {type searchableBox; min (-.05 -.10 -.10); max (1.2 .10 .10);} }
castellatedMeshControls {
 maxLocalCells 2000000; maxGlobalCells 2000000; minRefinementCells 0; maxLoadUnbalance 0.1;
 nCellsBetweenLevels 3; features ();
 refinementSurfaces {rocket {level (4 4); patchInfo {type wall;}}}
 resolveFeatureAngle 30;
 refinementRegions {wake {mode inside; levels ((1e15 1));}}
 locationInMesh (-.3 .2 .2); allowFreeStandingZoneFaces true;
}
snapControls {nSmoothPatch 3; tolerance 2; nSolveIter 30; nRelaxIter 5;
 nFeatureSnapIter 10; implicitFeatureSnap true; explicitFeatureSnap false; multiRegionFeatureSnap false;}
addLayersControls {}
meshQualityControls {
 maxNonOrtho 65; maxBoundarySkewness 20; maxInternalSkewness 3; maxConcave 80;
 minVol 1e-16; minTetQuality 1e-15; minArea -1; minTwist .02;
 minDeterminant .001; minFaceWeight .02; minVolRatio .01; minTriangleTwist -1;
 nSmoothScale 4; errorReduction .75;
}
mergeTolerance 1e-6;''')
    foam(out/'system/controlDict',f'''application simpleFoam;
startFrom startTime; startTime 0; stopAt endTime; endTime {iterations}; deltaT 1;
writeControl timeStep; writeInterval {iterations}; purgeWrite 0;
writeFormat binary; writePrecision 8; writeCompression off; timeFormat general; timePrecision 6;
runTimeModifiable false;
functions {{
 forces {{type forceCoeffs; libs ("libforces.so"); patches (rocket); rho rhoInf; rhoInf 1.225;
 CofR ({dry_cg*.001} 0 0); liftDir ({-math.sin(angle)} {math.cos(angle)} 0);
 dragDir ({math.cos(angle)} {math.sin(angle)} 0); pitchAxis (0 0 1);
 magUInf {speed}; lRef {2*r*.001}; Aref {refarea};
 writeControl timeStep; writeInterval 1; log true;}}
 yplus {{type yPlus; libs ("libfieldFunctionObjects.so"); writeControl writeTime;}}
}}''')
    foam(out/'system/fvSchemes','''ddtSchemes {default steadyState;}
gradSchemes {default Gauss linear; grad(U) cellLimited Gauss linear 1;}
divSchemes {default none; div(phi,U) bounded Gauss linearUpwindV grad(U);
 div(phi,k) bounded Gauss upwind; div(phi,omega) bounded Gauss upwind;
 div((nuEff*dev2(T(grad(U))))) Gauss linear;}
laplacianSchemes {default Gauss linear corrected;}
interpolationSchemes {default linear;} snGradSchemes {default corrected;}
wallDist {method meshWave;}''')
    foam(out/'system/fvSolution','''solvers {
 p {solver GAMG; smoother GaussSeidel; tolerance 1e-7; relTol .01;}
 "(U|k|omega)" {solver smoothSolver; smoother symGaussSeidel; tolerance 1e-8; relTol .1;}
}
SIMPLE {nNonOrthogonalCorrectors 1;}
relaxationFactors {fields {p .3;} equations {U .7; k .7; omega .7;}}''')
    foam(out/'constant/transportProperties','transportModel Newtonian; nu [0 2 -1 0 0 0 0] 1.5e-5;')
    foam(out/'constant/turbulenceProperties','simulationType RAS; RAS {RASModel kOmegaSST; turbulence on; printCoeffs on;}')
    for name,dim,value,wall in [('U','0 1 -1 0 0 0 0',velocity,'type noSlip;'),
        ('p','0 2 -2 0 0 0 0','0','type zeroGradient;'),
        ('k','0 2 -2 0 0 0 0',str(k),f'type kqRWallFunction; value uniform {k};'),
        ('omega','0 0 -1 0 0 0 0',str(omega),f'type omegaWallFunction; value uniform {omega};'),
        ('nut','0 2 -1 0 0 0 0','0','type nutkWallFunction; value uniform 0;')]:
        if name=='p':
            inlet='type zeroGradient;'
            outlet='type fixedValue; value uniform 0;'
        elif name=='nut':
            inlet=outlet='type calculated; value uniform 0;'
        else:
            inlet=f'type fixedValue; value uniform {value};'
            outlet=f'type inletOutlet; inletValue uniform {value}; value uniform {value};'
        foam(out/'0'/name,f'dimensions [{dim}]; internalField uniform {value};\n'
            'boundaryField {inlet {'+inlet+'} outlet {'+outlet+'} farfield {'+inlet+'} rocket {'+wall+'}}',
            'volVectorField' if name=='U' else 'volScalarField')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--cell-mm',type=float,default=40)
    parser.add_argument('--speed',type=float,default=40)
    parser.add_argument('--alpha',type=float,default=0)
    parser.add_argument('--iterations',type=int,default=600)
    parser.add_argument('--ring-chord-mm',type=int,choices=[0,5,10],default=0)
    args=parser.parse_args()
    if not 15<=args.cell_mm<=50 or not 10<=args.speed<=70 or not 0<=args.alpha<=10 or not 50<=args.iterations<=3000:
        parser.error('Pilot resource/flow bounds exceeded')
    generate(load_config(args.config),args.output,args.cell_mm,args.speed,args.alpha,args.iterations,args.ring_chord_mm)


if __name__=='__main__':
    main()
