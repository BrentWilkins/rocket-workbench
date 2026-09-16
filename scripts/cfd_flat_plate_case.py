"""Generate an OpenFOAM case from an official nested NASA TMR flat-plate grid."""

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

import numpy as np


GRID_MEMBERS = {
    35: 'flatplate_clust2_4levelsdown_35x25.p2dfmt',
    69: 'flatplate_clust2_3levelsdown_69x49.p2dfmt',
    137: 'flatplate_clust2_2levelsdown_137x97.p2dfmt',
    273: 'flatplate_clust2_1leveldown_273x193.p2dfmt.gz',
    545: 'flatplate_clust2.p2dfmt.gz',
}
ARCHIVE_SHA256 = '4b0a64c2c1648f696f92bf9a91e64e972e6c32e76e8daa70ffa65ed8dd641412'


def foam_header(cls: str, location: str, name: str) -> str:
    return (
        'FoamFile\n{\n version 2.0;\n format ascii;\n'
        f' class {cls};\n location "{location}";\n object {name};\n}}\n'
    )


def parse_plot3d(payload: bytes) -> tuple[np.ndarray, np.ndarray]:
    values=payload.decode().split()
    if int(values[0]) != 1:
        raise ValueError('Flat-plate PLOT3D input must contain exactly one block')
    ni,nj=map(int,values[1:3])
    count=ni*nj
    if len(values) != 3+2*count:
        raise ValueError('Unexpected formatted 2-D PLOT3D value count')
    x=np.asarray(values[3:3+count],dtype=float).reshape(nj,ni)
    y=np.asarray(values[3+count:],dtype=float).reshape(nj,ni)
    return x,y


def archive_grid(archive: Path, ni: int) -> tuple[np.ndarray,np.ndarray,dict]:
    digest=hashlib.sha256(archive.read_bytes()).hexdigest()
    if digest != ARCHIVE_SHA256:
        raise ValueError(f'TMR grid archive checksum mismatch: {digest}')
    suffix=GRID_MEMBERS[ni]
    with zipfile.ZipFile(archive) as bundle:
        names=[name for name in bundle.namelist() if name.endswith('/'+suffix)]
        if len(names) != 1:
            raise ValueError(f'Expected one archive member ending in {suffix}')
        info=bundle.getinfo(names[0])
        payload=bundle.read(info)
    if suffix.endswith('.gz'):
        import gzip
        payload=gzip.decompress(payload)
    x,y=parse_plot3d(payload)
    return x,y,{
        'archive_sha256': digest,
        'archive_member': names[0],
        'member_crc32': f'{info.CRC:08x}',
        'coordinate_payload_sha256': hashlib.sha256(payload).hexdigest(),
    }


def mesh_lists(x: np.ndarray,y: np.ndarray,span: float=0.01):
    nj,ni=x.shape
    if y.shape != x.shape or ni<2 or nj<2:
        raise ValueError('Invalid structured flat-plate grid dimensions')
    point=lambda k,j,i: k*nj*ni+j*ni+i
    cell=lambda j,i: j*(ni-1)+i
    points=[(float(x[j,i]),float(y[j,i]),z)
            for z in (-span/2,span/2) for j in range(nj) for i in range(ni)]
    internal=[]
    for j in range(nj-1):
        for i in range(1,ni-1):
            internal.append(((point(0,j,i),point(0,j+1,i),point(1,j+1,i),point(1,j,i)),
                             cell(j,i-1),cell(j,i)))
    for j in range(1,nj-1):
        for i in range(ni-1):
            internal.append(((point(0,j,i),point(1,j,i),point(1,j,i+1),point(0,j,i+1)),
                             cell(j-1,i),cell(j,i)))
    zero_indices=np.flatnonzero(np.isclose(x[0],0,rtol=0,atol=1e-14))
    if len(zero_indices)!=1:
        raise ValueError('Expected one flat-plate leading-edge point at x=0')
    leading=int(zero_indices[0])
    patches={name:[] for name in ('inlet','outlet','top','symmetry','plate','frontAndBack')}
    for j in range(nj-1):
        patches['inlet'].append(((point(0,j,0),point(1,j,0),point(1,j+1,0),point(0,j+1,0)),cell(j,0)))
        i=ni-1
        patches['outlet'].append(((point(0,j,i),point(0,j+1,i),point(1,j+1,i),point(1,j,i)),cell(j,i-1)))
    j=nj-1
    for i in range(ni-1):
        patches['top'].append(((point(0,j,i),point(1,j,i),point(1,j,i+1),point(0,j,i+1)),cell(j-1,i)))
    j=0
    for i in range(ni-1):
        target='symmetry' if i<leading else 'plate'
        patches[target].append(((point(0,j,i),point(0,j,i+1),point(1,j,i+1),point(1,j,i)),cell(j,i)))
    for j in range(nj-1):
        for i in range(ni-1):
            patches['frontAndBack'].append(((point(0,j,i),point(0,j+1,i),point(0,j+1,i+1),point(0,j,i+1)),cell(j,i)))
            patches['frontAndBack'].append(((point(1,j,i),point(1,j,i+1),point(1,j+1,i+1),point(1,j+1,i)),cell(j,i)))
    return points,internal,patches,leading


def write_mesh(folder: Path,x: np.ndarray,y: np.ndarray):
    points,internal,patches,leading=mesh_lists(x,y)
    poly=folder/'constant'/'polyMesh'
    poly.mkdir(parents=True)
    (poly/'points').write_text(foam_header('vectorField','constant/polyMesh','points')+
        f'{len(points)}\n(\n'+''.join(f'({a:.16g} {b:.16g} {c:.16g})\n' for a,b,c in points)+')\n')
    faces=[face for face,_,_ in internal]
    owners=[owner for _,owner,_ in internal]
    neighbours=[neighbour for _,_,neighbour in internal]
    starts={}
    for name,items in patches.items():
        starts[name]=len(faces)
        faces.extend(face for face,_ in items)
        owners.extend(owner for _,owner in items)
    (poly/'faces').write_text(foam_header('faceList','constant/polyMesh','faces')+
        f'{len(faces)}\n(\n'+''.join(f'4({" ".join(map(str,face))})\n' for face in faces)+')\n')
    for name,labels in (('owner',owners),('neighbour',neighbours)):
        (poly/name).write_text(foam_header('labelList','constant/polyMesh',name)+
            f'{len(labels)}\n(\n'+''.join(f'{label}\n' for label in labels)+')\n')
    entries=[]
    for name,items in patches.items():
        patch_type=('empty' if name=='frontAndBack' else
                    'symmetryPlane' if name=='symmetry' else
                    'wall' if name=='plate' else 'patch')
        entries.append(f'{name}\n{{ type {patch_type}; nFaces {len(items)}; startFace {starts[name]}; }}\n')
    (poly/'boundary').write_text(foam_header('polyBoundaryMesh','constant/polyMesh','boundary')+
        f'{len(entries)}\n(\n'+''.join(entries)+')\n')
    return {'points':len(points),'cells':(x.shape[0]-1)*(x.shape[1]-1),
            'faces':len(faces),'internal_faces':len(internal),'plate_leading_edge_i':leading}


def field(path: Path,dimensions: str,internal: str,boundaries: dict[str,str],cls='volScalarField'):
    path.parent.mkdir(parents=True,exist_ok=True)
    body=foam_header(cls,'0',path.name)+f'dimensions {dimensions};\ninternalField uniform {internal};\nboundaryField\n{{\n'
    body+=''.join(f' {name} {{ {condition} }}\n' for name,condition in boundaries.items())+'}\n'
    path.write_text(body)


def generate(archive: Path,out: Path,ni: int=69,iterations: int=2000,
             omega_wall: str='openfoam-blended',convection: str='first-order-upwind',
             sst_variant: str='openfoam-default',domain_top_y_m: float|None=None,
             solver_controls: str='conservative'):
    if ni not in GRID_MEMBERS:
        raise ValueError(f'Grid size must be one of {sorted(GRID_MEMBERS)}')
    if omega_wall not in ('openfoam-blended','tmr-fixed-factor10'):
        raise ValueError('Unknown omega wall treatment')
    if convection not in ('first-order-upwind','bounded-linear-upwind',
                           'linear-upwind-velocity'):
        raise ValueError('Unknown convection scheme')
    if sst_variant not in ('openfoam-default','tmr-sstm-flatplate-partial-map',
                            'tmr-sstm-v2512-source-map'):
        raise ValueError('Unknown SST variant')
    if (sst_variant in ('tmr-sstm-flatplate-partial-map',
                        'tmr-sstm-v2512-source-map') and
            omega_wall!='tmr-fixed-factor10'):
        raise ValueError('The TMR SSTm mapping requires the TMR factor-10 omega wall value')
    if solver_controls not in ('conservative','tmr-2014'):
        raise ValueError('Unknown solver controls')
    out.mkdir(parents=True,exist_ok=False)
    x,y,source=archive_grid(archive,ni)
    original_rows=int(y.shape[0])
    if domain_top_y_m is not None:
        if domain_top_y_m<=0:
            raise ValueError('Domain top height must be positive')
        row=int(np.argmin(np.abs(np.mean(y,axis=1)-domain_top_y_m)))
        if row<2 or row>=original_rows-1:
            raise ValueError('Requested domain top does not define a reduced usable grid')
        x=x[:row+1]
        y=y[:row+1]
    domain={'requested_top_y_m':domain_top_y_m,
            'selected_top_y_min_m':float(y[-1].min()),
            'selected_top_y_mean_m':float(y[-1].mean()),
            'selected_top_y_max_m':float(y[-1].max()),
            'original_rows':original_rows,'retained_rows':int(y.shape[0])}
    mesh=write_mesh(out,x,y)
    leading=mesh['plate_leading_edge_i']
    np.savez(out/'tmr-grid.npz',x=x,y=y)
    source['retained_coordinate_array_sha256']=hashlib.sha256(
        (out/'tmr-grid.npz').read_bytes()).hexdigest()
    velocity=1.0
    # TMR defines Re=5 million per unit length; the solid plate spans x=0..2.
    nu=2e-7
    intensity=0.00039
    nut_ratio=0.009
    k=1.5*(intensity*velocity)**2
    omega=k/(nut_ratio*nu)
    # Match the published TMR/OpenFOAM flat-plate table.  Earlier retained
    # cases used fixed values at the top and also fixed pressure at the inlet;
    # those artifacts remain untouched as non-acceptance evidence.
    common={'inlet':f'type fixedValue; value uniform {{value}};',
            'outlet':'type zeroGradient;','top':'type zeroGradient;',
            'symmetry':'type symmetryPlane;','plate':'type zeroGradient;','frontAndBack':'type empty;'}
    def bcs(value): return {name:text.format(value=value) for name,text in common.items()}
    ub=bcs('(1 0 0)'); ub['plate']='type noSlip;'
    field(out/'0'/'U','[0 1 -1 0 0 0 0]','(1 0 0)',ub,cls='volVectorField')
    pressure=bcs('0')
    pressure['inlet']='type zeroGradient;'
    pressure['outlet']='type fixedValue; value uniform 0;'
    field(out/'0'/'p','[0 2 -2 0 0 0 0]','0',pressure)
    kb=bcs(f'{k:.16g}'); kb['plate']='type fixedValue; value uniform 0;'
    field(out/'0'/'k','[0 2 -2 0 0 0 0]',f'{k:.16g}',kb)
    ob=bcs(f'{omega:.16g}')
    first_cell_wall_distance=float(np.mean((y[0,leading:-1]+y[1,leading:-1]+
                                            y[0,leading+1:]+y[1,leading+1:])/4))
    if omega_wall=='tmr-fixed-factor10':
        omega_wall_value=60*nu/(0.075*first_cell_wall_distance**2)
        ob['plate']=f'type fixedValue; value uniform {omega_wall_value:.16g};'
    else:
        omega_wall_value=None
        ob['plate']=f'type omegaWallFunction; value uniform {omega:.16g};'
    field(out/'0'/'omega','[0 0 -1 0 0 0 0]',f'{omega:.16g}',ob)
    freestream_nut=nut_ratio*nu
    nb=bcs(f'{freestream_nut:.16g}'); nb['plate']='type fixedValue; value uniform 0;'
    field(out/'0'/'nut','[0 2 -1 0 0 0 0]','0',nb)
    constant=out/'constant'; system=out/'system'; system.mkdir()
    (constant/'transportProperties').write_text(foam_header('dictionary','constant','transportProperties')+f'transportModel Newtonian;\nnu [0 2 -1 0 0 0 0] {nu};\n')
    if sst_variant in ('tmr-sstm-flatplate-partial-map','tmr-sstm-v2512-source-map'):
        coeff_name=('TmrSSTmCoeffs' if sst_variant=='tmr-sstm-v2512-source-map'
                    else 'kOmegaSSTCoeffs')
        sst_coeffs=(f' {coeff_name} {{ gamma1 0.5531666666666668; '
                    'gamma2 0.4403546666666667; c1 20; }')
    else:
        sst_coeffs=''
    ras_model=('TmrSSTm' if sst_variant=='tmr-sstm-v2512-source-map'
               else 'kOmegaSST')
    model_library=('libs ("libTmrSSTm.so");\n'
                   if sst_variant=='tmr-sstm-v2512-source-map' else '')
    (constant/'turbulenceProperties').write_text(
        foam_header('dictionary','constant','turbulenceProperties')+
        f'simulationType RAS;\nRAS {{ RASModel {ras_model}; turbulence on; '
        f'printCoeffs on;{sst_coeffs} }}\n')
    (system/'controlDict').write_text(foam_header('dictionary','system','controlDict')+
        model_library+f'application simpleFoam; startFrom startTime; startTime 0; stopAt endTime; endTime {iterations}; deltaT 1; writeControl timeStep; writeInterval {iterations}; writeFormat ascii; runTimeModifiable false; functions {{ wallShear {{ type wallShearStress; libs ("libfieldFunctionObjects.so"); patches (plate); writeControl writeTime; }} yplus {{ type yPlus; libs ("libfieldFunctionObjects.so"); writeControl writeTime; }} }}\n')
    if convection=='first-order-upwind':
        div_u=div_k=div_omega='bounded Gauss upwind'
    else:
        div_u='bounded Gauss linearUpwind grad(U)'
        div_k=('bounded Gauss upwind' if convection=='linear-upwind-velocity' else
               'bounded Gauss linearUpwind grad(k)')
        div_omega=('bounded Gauss upwind' if convection=='linear-upwind-velocity' else
                   'bounded Gauss linearUpwind grad(omega)')
    (system/'fvSchemes').write_text(foam_header('dictionary','system','fvSchemes')+f'ddtSchemes {{ default steadyState; }} gradSchemes {{ default Gauss linear; }} divSchemes {{ default none; div(phi,U) {div_u}; div(phi,k) {div_k}; div(phi,omega) {div_omega}; div((nuEff*dev2(T(grad(U))))) Gauss linear; }} laplacianSchemes {{ default Gauss linear corrected; }} interpolationSchemes {{ default linear; }} snGradSchemes {{ default corrected; }} wallDist {{ method meshWave; }}\n')
    if solver_controls=='tmr-2014':
        linear_tolerance='1e-20'; relative_tolerance='0'; pressure_relaxation='0.3'
        equation_relaxation='0.7'
    else:
        linear_tolerance='1e-9'; relative_tolerance='0.1'; pressure_relaxation='0.2'
        equation_relaxation='0.3'
    (system/'fvSolution').write_text(foam_header('dictionary','system','fvSolution')+
        f'solvers {{ p {{ solver PCG; preconditioner DIC; tolerance {linear_tolerance}; '
        f'relTol {relative_tolerance}; maxIter 1000; }} "(U|k|omega)" {{ solver PBiCGStab; '
        f'preconditioner DILU; tolerance {linear_tolerance}; relTol {relative_tolerance}; '
        f'maxIter 1000; }} }} SIMPLE {{ nNonOrthogonalCorrectors 0; residualControl {{ '
        f'p 1e-7; U 1e-7; k 1e-7; omega 1e-7; }} }} relaxationFactors {{ fields {{ '
        f'p {pressure_relaxation}; }} equations {{ U {equation_relaxation}; '
        f'k {equation_relaxation}; omega {equation_relaxation}; }} }}\n')
    manifest={'benchmark':'TMR 2DZP flat plate','scope':'wall_and_turbulence_subsystem_only',
              'grid_dimensions':[int(x.shape[1]),int(x.shape[0])], 'mesh':mesh,'source':source,
             'domain':domain,
             'boundary_conditions':{
                 'variant':'tmr-standard-sstm-flat-plate-table',
                 'transported_fields':{
                     'inlet':'fixedValue','outlet':'zeroGradient','top':'zeroGradient'},
                 'pressure':{
                     'inlet':'zeroGradient','outlet':'fixedValue','top':'zeroGradient'},
                 'wall_turbulence':{
                     'k':'fixedValue zero','omega':omega_wall,'nut':'fixedValue zero'},
                 'legacy_evidence_note':(
                     'Earlier cases either fixed pressure/top fields incorrectly or used '
                     'high-Re k/nut wall wrappers; preserve them as non-acceptance evidence.')},
             'conditions':{'U_m_s':velocity,'nu_m2_s':nu,'reference_length_m':2.0,
                            'Re_per_unit_length':velocity/nu,
                            'Re_plate_length':velocity*2/nu,'turbulence_intensity':intensity,
                           'freestream_nut_over_nu':nut_ratio,
                           'freestream_nut_m2_s':freestream_nut,
                           'k_m2_s2':k,'omega_s-1':omega},
              'model_mapping':{
                  'variant':sst_variant,
                 'openfoam_model':('OpenFOAM v2512 TmrSSTm runtime model'
                                   if sst_variant=='tmr-sstm-v2512-source-map'
                                   else 'OpenFOAM v2512 incompressible kOmegaSST'),
                 'tmr_target':'SSTm',
                 'equation_mapping_complete':sst_variant=='tmr-sstm-v2512-source-map',
                 'production_note':(
                     'v2512 source-derived model uses SSTm F1/F2, vorticity eddy-viscosity '
                     'limiter, strain-rate production, and incompressible m convention.'
                     if sst_variant=='tmr-sstm-v2512-source-map' else
                     'OpenFOAM strain-rate production is directionally aligned with SSTm, '
                     'but the full source-level mapping is incomplete.'),
                  'coefficient_overrides':({'gamma1':0.5531666666666668,
                                            'gamma2':0.4403546666666667,'c1':20}
                                           if sst_variant in ('tmr-sstm-flatplate-partial-map',
                                                              'tmr-sstm-v2512-source-map') else {}),
                 'known_unmapped_differences':(
                     ['F1/F2 implementation details and cross-diffusion floor',
                      'strain-rate rather than vorticity eddy-viscosity limiter invariant']
                     if sst_variant=='tmr-sstm-flatplate-partial-map' else [])},
              'omega_wall_treatment':{'variant':omega_wall,
                                      'first_cell_wall_distance_m':first_cell_wall_distance,
                                      'fixed_value_s-1':omega_wall_value,
                                      'tmr_formula':'10*6*nu/(beta1*d1^2), beta1=0.075'},
              'convection_scheme':convection,
              'solver_controls':solver_controls,
              'numerical_phase':('first-order upwind stabilized preflight; not benchmark-acceptance evidence'
                                 if convection=='first-order-upwind' else
                                 'higher-order sensitivity; acceptance still requires positivity and grid convergence'),
              'accepted_for_design':False}
    (out/'benchmark-spec.json').write_text(json.dumps(manifest,indent=2)+'\n')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--grid-archive',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--grid-ni',type=int,choices=sorted(GRID_MEMBERS),default=69)
    parser.add_argument('--iterations',type=int,default=2000)
    parser.add_argument('--omega-wall',choices=('openfoam-blended','tmr-fixed-factor10'),
                        default='openfoam-blended')
    parser.add_argument('--convection',choices=('first-order-upwind','bounded-linear-upwind',
                                                'linear-upwind-velocity'),
                        default='first-order-upwind')
    parser.add_argument('--sst-variant',choices=('openfoam-default',
                                                 'tmr-sstm-flatplate-partial-map',
                                                 'tmr-sstm-v2512-source-map'),
                        default='openfoam-default')
    parser.add_argument('--domain-top-y-m',type=float)
    parser.add_argument('--solver-controls',choices=('conservative','tmr-2014'),
                        default='conservative')
    args=parser.parse_args()
    generate(args.grid_archive,args.output,args.grid_ni,args.iterations,args.omega_wall,
             args.convection,args.sst_variant,args.domain_top_y_m,args.solver_controls)


if __name__=='__main__':
    main()
