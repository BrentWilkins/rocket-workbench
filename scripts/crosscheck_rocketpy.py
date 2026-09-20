"""RocketPy cross-check with shared OR mass/drag inputs, independent motion/surface model.

This is deliberately NOT an independent aerodynamic validation. Baseline Cd(M)
comes from each model's calm OpenRocket flight; nose/fins use RocketPy models.
"""
import argparse
import importlib.metadata
import json
import math
import warnings
import hashlib
import signal
from pathlib import Path

import numpy as np
from rocketpy import Environment, Flight, Function, GenericMotor, Rocket

from rocket_workbench.cli import save_json
from rocket_workbench.config import Config
from rocket_workbench.robustness import flight_metrics


def drag_tables(anchor):
    a = {k:np.asarray(v,dtype=float) for k,v in anchor["timeseries"].items()}
    burnout = anchor["metrics"]["burnout_time_s"]
    apogee = next(e["time_s"] for e in anchor["events"] if e["type"]=="APOGEE")
    tables = []
    for mask in (a["time_s"] <= burnout, (a["time_s"] > burnout) & (a["time_s"] < apogee)):
        mask &= np.isfinite(a["drag_coefficient"]) & (a["speed_m_s"]>3) & (a["drag_coefficient"]>0)
        x,y = a["mach"][mask], a["drag_coefficient"][mask]
        order=np.argsort(x); x,idx=np.unique(x[order],return_index=True); y=y[order][idx]
        if len(x)<2:
            raise ValueError("Insufficient calm-flight drag samples")
        tables.append(np.c_[np.r_[0,x,1],np.r_[y[0],y,y[-1]]])
    return tables


def build(config, native, motor_record, anchor):
    mass=native["mass_audit"]; g=config.geometry; mm=g.mm
    on,off=drag_tables(anchor)
    rocket=Rocket(radius=mm("body_od")/2000, mass=mass["dry_mass_g"]/1000,
        inertia=(mass["dry_pitch_inertia_kg_m2"],mass["dry_pitch_inertia_kg_m2"],mass["dry_roll_inertia_kg_m2"]),
        power_on_drag=Function(on,interpolation="linear",extrapolation="constant"),
        power_off_drag=Function(off,interpolation="linear",extrapolation="constant"),
        center_of_mass_without_motor=mass["dry_cg_x_mm"]/1000,
        coordinate_system_orientation="nose_to_tail")
    mr=motor_record; length=mr["length_mm"]/1000; radius=mr["diameter_mm"]/2000
    dry=mr["spent_mass_g"]/1000; loaded=mr["loaded_mass_g"]/1000
    times=np.asarray(mr["time_s"]); cg=np.asarray(mr["cg_from_front_mm"])/1000
    if np.ptp(cg)>1e-9:
        raise ValueError("This adapter requires the selected constant-CG motor curves")
    motor=GenericMotor(thrust_source=np.c_[times,mr["thrust_n"]],burn_time=(0,float(times[-1])),
        chamber_radius=radius,chamber_height=length,chamber_position=float(cg[0]),
        propellant_initial_mass=loaded-dry,nozzle_radius=0, dry_mass=dry,
        center_of_dry_mass_position=float(cg[0]),dry_inertia=(dry*(3*radius**2+length**2)/12,)*2+(dry*radius**2/2,),
        nozzle_position=length,coordinate_system_orientation="combustion_chamber_to_nozzle")
    # Use the same mass-vs-time samples, not a second propellant depletion assumption.
    motor.propellant_mass=Function(np.c_[times,np.asarray(mr["mass_g"])/1000-dry],
                                  interpolation="linear",extrapolation="constant")
    slopes=np.diff(np.asarray(mr["mass_g"])/1000)/np.diff(times)
    motor.total_mass_flow_rate=Function(lambda t: float(slopes[min(np.searchsorted(times,float(np.real(t)),side="right")-1,len(slopes)-1)])
                                       if 0<=float(np.real(t))<times[-1] else 0.)
    motor_cg=(mass["launch_mass_g"]*mass["launch_cg_x_mm"]-mass["dry_mass_g"]*mass["dry_cg_x_mm"])/mr["loaded_mass_g"]/1000
    rocket.add_motor(motor,position=motor_cg-float(cg[0]))
    # Avoid re-interpolating nonlinear derived CG/inertia on sparse thrust knots.
    # All axes below are the RocketPy dry-CG axes, except center_of_mass itself.
    structure_mass=mass["dry_mass_g"]/1000
    structure_cg=mass["dry_cg_x_mm"]/1000
    prop_mass=motor.propellant_mass
    total_mass=lambda t: structure_mass+dry+prop_mass(t)
    rocket.total_mass=Function(total_mass)
    rocket.center_of_mass=Function(lambda t: (structure_mass*structure_cg+(dry+prop_mass(t))*motor_cg)/total_mass(t))
    unit_pitch=(3*radius**2+length**2)/12
    rocket.I_11=Function(lambda t: rocket.dry_I_11+prop_mass(t)*(unit_pitch+(motor_cg-rocket.center_of_dry_mass_position)**2))
    rocket.I_22=rocket.I_11
    rocket.I_33=Function(lambda t: rocket.dry_I_33+prop_mass(t)*radius**2/2)
    rocket.com_to_cdm_function=Function(lambda t: -(motor_cg-rocket.center_of_dry_mass_position)*rocket._csys*prop_mass(t)/total_mass(t))
    rocket.add_nose(length=mm("nose_length")/1000,kind=config.nose_shape,position=0)
    collar=(mm("nose_length")+mm("body_length")-mm("collar_length"))/1000
    collar_radius=(mm("body_od")/2+mm("clearance")+mm("wall"))/1000
    rocket.add_tail(top_radius=mm("body_od")/2000,bottom_radius=collar_radius,
                    length=mm("fairing_length")/1000,position=collar-mm("fairing_length")/1000)
    rocket.add_trapezoidal_fins(n=3,root_chord=mm("fin_root")/1000,
        tip_chord=.2*mm("fin_root")/1000,span=mm("fin_span")/1000,
        sweep_length=.8*mm("fin_root")/1000,position=collar,radius=collar_radius)
    deployment=float(times[-1])+mr["delay_s"]+.001
    # Arm at t=0 and use a fixed timer to reproduce native burnout+delay ejection.
    # No callback-count clock: solver/event scheduling can call a trigger repeatedly.
    rocket.add_parachute("motor-ejection proxy",cd_s=config.chute_cd.value*math.pi*(mm("chute_diameter")/2000)**2,
                         trigger=lambda pressure,height,state: True,sampling_rate=100,lag=deployment)
    audit=dict(launch_mass_g=float(rocket.total_mass(0)*1000),
               launch_cg_x_mm=float(rocket.center_of_mass(0)*1000),
               # RocketPy I_11 is about dry CG; OR reports about instantaneous CG.
               launch_pitch_inertia_kg_m2=float(rocket.I_11(0)-rocket.total_mass(0)*
                   (rocket.center_of_mass(0)-rocket.center_of_dry_mass_position)**2),
               launch_roll_inertia_kg_m2=float(rocket.I_33(0)),
               motor_front_m=motor_cg-float(cg[0]),burnout_s=float(times[-1]),
               deployment_requested_s=deployment)
    for k in ("launch_mass_g","launch_cg_x_mm"):
        if abs(audit[k]-mass[k])>1e-5:
            raise ValueError(f"RocketPy input mismatch {k}: {audit[k]} != {mass[k]}")
    for k in ("launch_pitch_inertia_kg_m2","launch_roll_inertia_kg_m2"):
        audit[k+"_relative_delta"]=(audit[k]-mass[k])/mass[k]
        if abs(audit[k+"_relative_delta"])>.01:
            raise ValueError(f"RocketPy inertia mismatch >1%: {k}")
    atmosphere=np.asarray(native["atmosphere"]["levels"])
    env=Environment(latitude=config.launch.latitude.value,longitude=config.launch.longitude.value,
        elevation=config.launch.elevation.value,gravity=np.c_[atmosphere[:,0],atmosphere[:,3]],max_expected_height=3000)
    wind=np.asarray(native["inputs"]["wind"]["levels"],dtype=float).copy();wind[:,0]+=config.launch.elevation.value
    env.set_atmospheric_model(type="custom_atmosphere",pressure=atmosphere[:,:2],
        temperature=np.c_[atmosphere[:,0],atmosphere[:,2]],wind_u=wind[:,[0,1]],wind_v=wind[:,[0,2]])
    return rocket,env,audit


def _crosscheck(config,native,motor,anchor,max_step=.01):
    rocket,env,audit=build(config,native,motor,anchor)
    # Barrowman's small-angle lift law is singular in nearly axial reversed flow.
    # Compare ballistic ascent only; do not invent a reverse-flow aerodynamic fix.
    rocket.parachutes.clear()
    s=native["inputs"]
    # No rail buttons: directly pass OR's audited effective travel, rather than
    # accidentally subtracting a second (and different) lug/button offset.
    flight=Flight(rocket=rocket,environment=env,rail_length=native["effective_guide_m"],
        inclination=90-s["tilt_deg"],heading=s["tilt_heading_deg"],max_time=300,
        max_time_step=max_step,rtol=1e-7,atol=1e-9,time_overshoot=False,verbose=False,
        terminate_on_apogee=True)
    end=float(flight.t_final); burnout=audit["burnout_s"]
    t=np.unique(np.r_[np.asarray(flight.solution)[:,0],float(flight.out_of_rail_time),burnout,
                      float(flight.apogee_time),end])
    t=t[(t>=0)&(t<=end)]
    def values(name):return np.array([getattr(flight,name)(float(x)) for x in t])
    theta=values("attitude_angle") # RocketPy degrees from horizontal
    a=dict(time_s=t,altitude_m=values("z")-env.elevation,velocity_z_m_s=values("vz"),
           speed_m_s=values("speed"),east_m=values("x"),north_m=values("y"),
           angle_of_attack_rad=np.radians(values("angle_of_attack")),orientation_theta_rad=np.radians(theta),
           pitch_rate_rad_s=values("w1"),yaw_rate_rad_s=values("w2"),roll_rate_rad_s=values("w3"),
           thrust_n=np.array([rocket.motor.thrust(float(x)) for x in t]),
           cg_x_m=np.array([rocket.center_of_mass(float(x)) for x in t]),
           cp_x_m=np.array([rocket.cp_position(float(x)) for x in values("mach_number")]),
           reference_length_m=np.full(len(t),config.geometry.mm("body_od")/1000))
    events=[dict(type=k,time_s=float(v)) for k,v in [("LAUNCHROD",flight.out_of_rail_time),
            ("BURNOUT",burnout),("APOGEE",flight.apogee_time)] if v is not None and 0<=v<=end]
    result=dict(design=native["design"],scenario=native["scenario"],engine="RocketPy",
        execution="completed" if float(flight.apogee)>env.elevation and abs(float(flight.apogee_time)-end)<1e-6 else "simulation failed",
        scope="ascent_only", recovery_model="disabled: ballistic ascent stops at apogee",
        planned_ejection_precedes_ballistic_apogee=audit["deployment_requested_s"]<float(flight.apogee_time),
        warnings=[],events=events,timeseries={k:v.tolist() for k,v in a.items()},inputs=s,
        mass_audit=audit,effective_guide_m=native["effective_guide_m"],timestep_s=max_step)
    result["metrics"]=dict(apogee_m=float(flight.apogee-env.elevation),
        guide_departure_m_s=float(flight.out_of_rail_velocity),
        deployment_speed_m_s=None,deployment_time_s=None,landing_displacement_m=None,
        landing_east_m=None,landing_north_m=None,landing_descent_m_s=None,**flight_metrics(result))
    return result


def crosscheck(config,native,motor,anchor,max_step=.01):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result=_crosscheck(config,native,motor,anchor,max_step)
    result["warnings"] = sorted({str(w.message) for w in caught})
    result["coverage_note"] = "Powered flight and ballistic apogee only; no recovery, descent or landing cross-check"
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--limit",type=int,default=0)
    p.add_argument("--label",default="rocketpy")
    p.add_argument("--timeout",type=int,default=120)
    args=p.parse_args();dest=args.output/args.label;dest.mkdir(exist_ok=True)
    digest=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if (dest/"runtime.json").exists() and json.loads((dest/"runtime.json").read_text()).get("source_sha256")!=digest:
        raise ValueError("Adapter changed; select a fresh --label to retain failed evidence")
    save_json(dest/"runtime.json",dict(rocketpy=importlib.metadata.version("rocketpy"),source_sha256=digest,
        drag="shared calm OR Cd(M), separate powered/coast curves; endpoint held",
        independent="motion integration and native RocketPy nose/fin/tail normal-force models",
        turbulence="no RocketPy equivalent imposed; turbulent OR cases excluded",
        scope="ascent_only; recovery disabled; terminate_on_apogee=True",
        limitation="Nearly axial reversed flow makes native Barrowman lift direction singular; conical D12 calm stalled at t~6.57556s before ejection",
        diagnostic_evidence="runs/robustness-20260919-v2 retained failed full-flight cross-checks; a +/-1e-7 m/s lateral-velocity perturbation changed pitch acceleration from -1.205 to +1.957 rad/s^2",
        guide="OR effective travel passed directly, no additional button offsets"))
    for source in sorted((args.output/"deterministic").glob("*.jsonl")):
        folder=args.output/source.stem;cfg=Config.model_validate_json((folder/"nominal.json").read_text())
        mr=json.loads((folder/"motor.json").read_text())
        rows=[json.loads(l) for l in source.read_text().splitlines()]
        anchor=next(r for r in rows if r["scenario"]=="rod0.9144-wind0-heading0")
        rows=[r for r in rows if r["inputs"]["turbulence_m_s"]==0]
        if args.limit:rows=rows[:args.limit]
        path=dest/source.name;done=set()
        if path.exists():done={json.loads(l)["scenario"] for l in path.read_text().splitlines()}
        for row in rows:
            if row["scenario"] in done:continue
            try:
                def expired(signum,frame):raise TimeoutError(f"RocketPy case exceeded {args.timeout} seconds")
                signal.signal(signal.SIGALRM,expired);signal.alarm(args.timeout)
                r=crosscheck(cfg,row,mr,anchor)
            except Exception as exc:
                r=dict(design=source.stem,scenario=row["scenario"],engine="RocketPy",execution="simulation failed",
                       error=f"{type(exc).__name__}: {exc}",metrics={})
            finally:signal.alarm(0)
            with path.open("a") as f:f.write(json.dumps(r,allow_nan=False)+"\n")
            print(source.stem,row["scenario"],r["execution"],r.get("error"),flush=True)


if __name__=="__main__":main()
