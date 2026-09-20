"""Render a reproducible, partial-run-safe flight robustness report (no simulation)."""
from __future__ import annotations

import argparse
from collections import defaultdict
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

METRICS = {
    "apogee_m": "Apogee (m)",
    "guide_departure_m_s": "Guide-exit speed (m/s)",
    "powered_min_stability_cal": "Powered minimum stability (cal)",
    "minimum_ascent_stability_cal": "Whole-ascent minimum stability (cal)",
    "powered_max_aoa_deg": "Powered maximum angle of attack (°)",
    "burnout_tilt_deg": "Nose tilt at burnout (°)",
    "powered_max_pitch_yaw_rate_deg_s": "Maximum pitch/yaw rate (°/s)",
    "deployment_speed_m_s": "Deployment speed (m/s)",
    "landing_displacement_m": "Landing displacement (m)",
}
PAIRED = ("apogee_m", "powered_min_stability_cal", "burnout_tilt_deg")
COLORS = {"b500-n50-conical": "#9a6f38", "b500-n40-ogive": "#137eab", "b530-n40-ogive": "#bd4374"}


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and np.isfinite(value)


def rank_correlation(x,y):
    """Spearman correlation using average ranks for ties; NumPy-only reporting."""
    def ranks(values):
        a=np.asarray(values); order=np.argsort(a,kind="stable"); result=np.empty(len(a),dtype=float)
        boundaries=np.r_[0,np.flatnonzero(np.diff(a[order]))+1,len(a)]
        for start,end in zip(boundaries[:-1],boundaries[1:]):
            result[order[start:end]]=(start+end-1)/2
        return result
    return float(np.corrcoef(ranks(x),ranks(y))[0,1])


def value(row, metric):
    if row.get("engine")=="OpenRocket" and metric.startswith("powered_") and not row.get("metrics",{}).get("powered_data_complete"):
        return None
    v = row.get("metrics", {}).get(metric)
    return float(v) if row.get("execution") == "completed" and finite(v) else None


def statistics(values, expected=None, bootstrap=600):
    """Quantiles conditional on available data; never relabel missing rows as successes."""
    a = np.asarray([v for v in values if finite(v)], dtype=float)
    result = dict(expected=len(values) if expected is None else expected, valid=len(a))
    if result["expected"] < len(values):
        raise ValueError("Expected denominator is smaller than the observed sample count")
    result["missing"] = result["expected"] - len(a)
    result.update(quantiles=None, ci95=None)
    if len(a):
        result["quantiles"] = np.quantile(a, [.05, .5, .95]).tolist()
        if len(a) > 1:
            rng = np.random.default_rng(71492)
            q = np.quantile(rng.choice(a, (bootstrap, len(a))), [.05, .5, .95], axis=1)
            result["ci95"] = np.quantile(q, [.025, .975], axis=1).T.tolist()
    return result


def threshold_count(rows,metric,threshold,side,expected):
    vals=[value(r,metric) for r in rows]
    valid=[v for v in vals if v is not None]
    count=sum(v<threshold if side=="below" else v>threshold for v in valid)
    return dict(metric=metric,threshold=threshold,side=side,expected=expected,valid=len(valid),missing=expected-len(valid),
                beyond=count,fraction_of_valid=count/len(valid) if valid else None)


def paired_rows(rows, motor, metric, seed=None, limit=None):
    """Pair only exact sample identities; preserve missing partners as None."""
    groups = defaultdict(dict)
    for r in rows:
        inp = r["inputs"]
        if "master_seed" not in inp or not r["design"].endswith(motor):
            continue
        if seed is not None and inp["master_seed"] != seed:
            continue
        if limit is not None and inp["index"] >= limit:
            continue
        if r["design"] in (f"b500-n40-ogive-{motor}", f"b530-n40-ogive-{motor}"):
            groups[(inp["master_seed"], inp["index"])][r["design"][:4]] = value(r, metric)
    return [p["b530"] - p["b500"] if p.get("b530") is not None and p.get("b500") is not None else None
            for _, p in sorted(groups.items())]


def load(root):
    rows, hashes, incomplete = [], {}, []
    paths = sorted(root.glob("deterministic/*.jsonl")) + sorted(root.glob("ensemble-*/*.jsonl"))
    for path in paths:
        raw = path.read_bytes()
        hashes[str(path)] = hashlib.sha256(raw).hexdigest()
        lines = raw.splitlines()
        for i, line in enumerate(lines):
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                if i == len(lines)-1 and not raw.endswith(b"\n"):
                    incomplete.append(str(path))
                    continue
                raise
            row["phase"] = path.parent.name
            rows.append(row)
    keys = [(r["phase"], r["design"], r["scenario"]) for r in rows]
    if len(set(keys)) != len(keys):
        raise ValueError("Duplicate phase/design/scenario; cannot count independent samples")
    return rows, hashes, incomplete


def verify_snapshot(root,study,rows,require_complete=False):
    manifest_bytes=(root/"samples.json").read_bytes()
    if hashlib.sha256(manifest_bytes).hexdigest()!=study["samples_sha256"]:
        raise ValueError("Sample manifest does not match the frozen study")
    for relative,digest in study.get("files_sha256",{}).items():
        if hashlib.sha256((root/relative).read_bytes()).hexdigest()!=digest:
            raise ValueError(f"Study model/source snapshot changed: {relative}")
    manifest={s["id"]:s for s in json.loads(manifest_bytes)}
    expected={(f'ensemble-{s["master_seed"]}',model,s["id"]) for s in manifest.values() for model in study["models"]}
    seen=set()
    for row in rows:
        if row["phase"].startswith("ensemble-"):
            key=(row["phase"],row["design"],row["scenario"])
            if key not in expected or row["inputs"]!=manifest[row["scenario"]]:
                raise ValueError("Ensemble result does not match its shared sample manifest")
            seen.add(key)
    if require_complete:
        if seen!=expected:
            raise ValueError(f"Final report requires complete campaign: missing {len(expected-seen)} ensemble rows")
        counts={m:sum(r["phase"]=="deterministic" and r["design"]==m for r in rows) for m in study["models"]}
        if any(n<20 for n in counts.values()):
            raise ValueError("Final report requires all deterministic cases")


def save(fig, out, name, title):
    fig.suptitle(title)
    fig.text(.5, .005, "Conditional model results · assumed engineering bounds · not measured flight reliability", ha="center", fontsize=8)
    fig.tight_layout(rect=(0, .025, 1, .96))
    for ext in ("svg", "png"):
        fig.savefig(out / f"{name}.{ext}", dpi=160)
    plt.close(fig)


def render(rows, study, out):
    det = [r for r in rows if r["phase"] == "deterministic"]
    ens = [r for r in rows if r["phase"].startswith("ensemble-")]
    fig, axes = plt.subplots(4, 2, figsize=(12, 12))
    for col, motor in enumerate(("D12", "E12")):
        for j, metric in enumerate(("guide_departure_m_s", "powered_max_aoa_deg", "powered_min_stability_cal", "burnout_tilt_deg")):
            ax = axes[j, col]
            for model in study["models"]:
                if not model.endswith(motor):
                    continue
                for guide, style in ((.9144, "-"), (1.524, "--")):
                    cases = [r for r in det if r["design"] == model and r["scenario"].startswith(f"rod{guide:g}-wind") and r["scenario"].endswith("heading0") and value(r, metric) is not None]
                    cases.sort(key=lambda r: np.linalg.norm(r["inputs"]["wind"]["levels"][0][1:]))
                    ax.plot([np.linalg.norm(r["inputs"]["wind"]["levels"][0][1:]) for r in cases], [value(r, metric) for r in cases], style, marker="o", color=COLORS[model.rsplit("-", 1)[0]], label=model.rsplit("-", 1)[0]+(" · 36 in" if guide < 1 else " · 60 in"))
            ax.set(xlabel="Constant wind toward north (m/s)", ylabel=METRICS[metric], title=motor)
            ax.grid(alpha=.2)
    axes[0, 0].legend(fontsize=7)
    save(fig, out, "deterministic", "Wind and launch-guide comparison · nominal masses")

    fig, axes = plt.subplots(3, 2, figsize=(11, 10))
    for col, motor in enumerate(("D12", "E12")):
        for j, metric in enumerate(PAIRED):
            vals = [v for v in paired_rows(ens, motor, metric) if v is not None]
            ax = axes[j, col]
            ax.hist(vals, bins=35, color="#137eab", alpha=.8)
            ax.axvline(0, color="black", linestyle="--")
            ax.set(xlabel="530 minus 500 mm: " + METRICS[metric], ylabel="Valid paired samples", title=f"{motor} · {len(vals)} pairs")
    save(fig, out, "paired-differences", "What does another 30 mm change? · paired ogive designs")

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    for ax, motor in zip(axes, ("D12", "E12")):
        for model in study["models"]:
            cases = [r for r in ens if r["design"] == model and model.endswith(motor) and value(r, "landing_east_m") is not None and value(r, "landing_north_m") is not None]
            if cases:
                ax.scatter([value(r, "landing_east_m") for r in cases], [value(r, "landing_north_m") for r in cases], s=5, alpha=.22, color=COLORS[model.rsplit("-",1)[0]], label=model.rsplit("-",1)[0])
        ax.set(xlabel="East displacement (m)", ylabel="North displacement (m)", title=motor, aspect="equal")
        ax.legend(fontsize=7)
    save(fig, out, "landing", "Synthetic-weather landing cloud · unvalidated recovery assumptions")

    fig, axes = plt.subplots(3, 2, figsize=(11, 10))
    convergence = []
    for col, motor in enumerate(("D12", "E12")):
        for j, metric in enumerate(PAIRED):
            ax = axes[j, col]
            for seed, color in zip(study["seeds"], ("#137eab", "#bd4374")):
                for qidx, ls in enumerate((":", "-", "--")):
                    xs, ys = [], []
                    for n in (100, 500, 1000):
                        vals = paired_rows(ens, motor, metric, seed, n)
                        s = statistics(vals, n)
                        if qidx == 0:
                            convergence.append(dict(motor=motor, metric=metric, seed=seed, prefix=n, **s))
                        if s["valid"] == n:
                            xs.append(n); ys.append(s["quantiles"][qidx])
                            lo, hi = s["ci95"][qidx]
                            ax.vlines(n, lo, hi, color=color, alpha=.3)
                    ax.plot(xs, ys, ls, marker="o", color=color, label=f"{seed} P{(5,50,95)[qidx]}")
            ax.set(xlabel="Complete pairs per seed", ylabel="Δ " + METRICS[metric], title=motor)
    axes[0, 0].legend(fontsize=6, ncol=2)
    save(fig, out, "convergence", "Paired quantile convergence · bars: 95% percentile-bootstrap intervals")

    sensitivities = []
    fig, axes = plt.subplots(1, 2, figsize=(12, 7))
    for ax, motor in zip(axes, ("D12", "E12")):
        cases = [r for r in ens if r["design"] == f"b530-n40-ogive-{motor}"]
        fields = sorted({k for r in cases for k in r["inputs"] if k.startswith("mass:") or k in ("finish_g", "wind_speed_m_s", "shear_m_s", "veer_deg", "tilt_deg", "turbulence_m_s")})
        ranks = []
        for field in fields:
            pairs = [(r["inputs"][field], value(r, "powered_max_aoa_deg")) for r in cases if finite(r["inputs"].get(field)) and value(r, "powered_max_aoa_deg") is not None]
            if len(pairs)>2 and np.ptp(np.asarray(pairs)[:, 0])>0 and np.ptp(np.asarray(pairs)[:, 1])>0:
                rho = rank_correlation(*zip(*pairs))
                ranks.append((field, rho))
                sensitivities.append(dict(motor=motor, design=f"b530-n40-ogive-{motor}", metric="powered_max_aoa_deg", input=field, rho=rho, valid=len(pairs)))
        ranks.sort(key=lambda p: abs(p[1]))
        ax.barh([p[0] for p in ranks], [p[1] for p in ranks], color="#137eab")
        ax.set(xlim=(-1,1), xlabel="Spearman rank correlation", title=motor)
    save(fig, out, "sensitivity", "530 mm ogive: sensitivity of powered maximum angle of attack")
    return convergence, sensitivities


def interactive(rows, out):
    traces = []
    for row in rows:
        t = row.get("timeseries")
        if not t:
            continue
        # Actual retained samples only; decimation limits browser cost, not metric calculations.
        indexes = np.unique(np.r_[np.arange(0,len(t["time_s"]),5),len(t["time_s"])-1]).astype(int)
        traces.append(dict(design=row["design"], scenario=row["scenario"], phase=row["phase"],
            events=row.get("events",[]),
            data={k:[t[k][i] for i in indexes] for k in ("time_s","east_m","north_m","altitude_m","orientation_theta_rad","angle_of_attack_rad","cp_x_m","cg_x_m","reference_length_m")}))
    template = '''<!doctype html><meta charset="utf-8"><title>Flight robustness: retained traces</title>
<style>body{font:16px system-ui;margin:2rem;max-width:1200px;background:#fafafa}select{margin:.5rem;padding:.4rem}canvas{background:white;width:100%;border:1px solid #ccc}p{max-width:1000px}</style>
<h1>Paired flight comparison</h1><p>OpenRocket, corrected effective guide travel. Recorded deterministic flights and first five ensemble traces per seed only—not the complete Monte Carlo cloud. Curves use every fifth retained timestep; reported extrema use full data.</p>
<label>Motor <select id="motor"><option>D12</option><option>E12</option></select></label>
<label>Scenario <select id="scenario"></select></label>
<label>View <select id="view"><option value="trajectory">East–altitude trajectory</option><option value="north">North–altitude trajectory</option><option value="aoa">Angle of attack versus time</option><option value="tilt">Nose tilt versus time</option><option value="stability">Stability versus time</option></select></label>
<label><input id="powered" type="checkbox" checked>Through burnout only</label><canvas id="plot" width="1200" height="650"></canvas><p id="legend"></p><p>Launch-guide exit (circle) and burnout (square) marked at nearest retained timestep. Small angle of attack does not imply a near-vertical trajectory. Sampled bounds are assumptions, not measured likelihoods; recovery aerodynamics and motor variability remain unvalidated.</p>
<script>const traces=__DATA__;const colors={'b500-n50-conical':'#9a6f38','b500-n40-ogive':'#137eab','b530-n40-ogive':'#bd4374'};
const sel=document.getElementById('scenario');for(const s of [...new Set(traces.map(r=>r.scenario))]){let o=document.createElement('option');o.textContent=s;sel.appendChild(o)}
function draw(){const c=document.getElementById('plot'),g=c.getContext('2d');g.clearRect(0,0,c.width,c.height);let view=document.getElementById('view').value,phase=document.getElementById('powered').checked;let rr=traces.filter(r=>r.scenario===sel.value&&r.design.endsWith(document.getElementById('motor').value));let lines=rr.map(r=>{let d=r.data,b=r.events.find(e=>e.type==='BURNOUT')?.time_s??Infinity;return {r,p:d.time_s.map((t,i)=>{let x=view==='trajectory'?d.east_m[i]:view==='north'?d.north_m[i]:t;let y=view==='trajectory'||view==='north'?d.altitude_m[i]:view==='aoa'?d.angle_of_attack_rad[i]*180/Math.PI:view==='tilt'?Math.abs(Math.PI/2-d.orientation_theta_rad[i])*180/Math.PI:(d.cp_x_m[i]-d.cg_x_m[i])/d.reference_length_m[i];return [x,y,t]}).filter(p=>(!phase||p[2]<=b)&&Number.isFinite(p[0])&&Number.isFinite(p[1]))}});let all=lines.flatMap(l=>l.p);if(!all.length)return;let xs=all.map(p=>p[0]),ys=all.map(p=>p[1]);let xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);if(xmax-xmin<.01){xmin-=.01;xmax+=.01}if(ymax-ymin<.01){ymin-=.01;ymax+=.01}let X=x=>80+(x-xmin)/(xmax-xmin)*1080,Y=y=>580-(y-ymin)/(ymax-ymin)*530;g.font='15px system-ui';for(let i=0;i<6;i++){let x=xmin+(xmax-xmin)*i/5,y=ymin+(ymax-ymin)*i/5;g.strokeStyle='#eee';g.beginPath();g.moveTo(X(x),50);g.lineTo(X(x),580);g.moveTo(80,Y(y));g.lineTo(1160,Y(y));g.stroke();g.fillStyle='#333';g.fillText(x.toFixed(2),X(x)-18,608);g.fillText(y.toFixed(2),5,Y(y)+5)}g.fillText(view==='trajectory'?'East (m)':view==='north'?'North (m)':'Time (s)',550,640);g.fillText(view==='trajectory'||view==='north'?'Altitude AGL (m)':view==='stability'?'Stability (cal)':'Angle (degrees)',80,25);for(let l of lines){g.strokeStyle=g.fillStyle=colors[l.r.design.replace(/-[DE]12$/,'')];g.lineWidth=2;g.beginPath();l.p.forEach((p,i)=>i?g.lineTo(X(p[0]),Y(p[1])):g.moveTo(X(p[0]),Y(p[1])));g.stroke();for(let type of ['LAUNCHROD','BURNOUT']){let e=l.r.events.find(e=>e.type===type);if(!e||!l.p.length)continue;let p=l.p.reduce((a,b)=>Math.abs(a[2]-e.time_s)<Math.abs(b[2]-e.time_s)?a:b);if(type==='BURNOUT')g.fillRect(X(p[0])-4,Y(p[1])-4,8,8);else{g.beginPath();g.arc(X(p[0]),Y(p[1]),4,0,7);g.fill()}}}document.getElementById('legend').innerHTML=lines.map(l=>'<span style="color:'+colors[l.r.design.replace(/-[DE]12$/,'')]+'">● '+l.r.design+'</span>').join(' &nbsp; ')}document.querySelectorAll('select,input').forEach(e=>e.onchange=draw);draw();</script>'''
    # Trajectory axes use the same metres-per-pixel scale: millimetre calm-air drift
    # must not look like a large turn simply because the horizontal axis auto-zooms.
    template=template.replace("let X=x=>", "if(view==='trajectory'||view==='north'){let xc=(xmin+xmax)/2,yc=(ymin+ymax)/2,w=Math.max(xmax-xmin,(ymax-ymin)*1080/530),h=w*530/1080;xmin=xc-w/2;xmax=xc+w/2;ymin=yc-h/2;ymax=yc+h/2}let X=x=>")
    template=template.replace("function draw(){", "if([...sel.options].some(o=>o.value==='rod0.9144-wind4-heading90'))sel.value='rod0.9144-wind4-heading90';function draw(){")
    template=template.replace("function draw(){", "const query=new URLSearchParams(location.search);for(const id of ['motor','scenario','view']){let el=document.getElementById(id),v=query.get(id);if(v&&[...el.options].some(o=>o.value===v))el.value=v}function draw(){")
    template=template.replace("d.angle_of_attack_rad[i]*180/Math.PI", "(Number.isFinite(d.angle_of_attack_rad[i])?d.angle_of_attack_rad[i]*180/Math.PI:NaN)")
    template=template.replace("Math.abs(Math.PI/2-d.orientation_theta_rad[i])*180/Math.PI", "(Number.isFinite(d.orientation_theta_rad[i])?Math.abs(Math.PI/2-d.orientation_theta_rad[i])*180/Math.PI:NaN)")
    template=template.replace("(d.cp_x_m[i]-d.cg_x_m[i])/d.reference_length_m[i]", "([d.cp_x_m[i],d.cg_x_m[i],d.reference_length_m[i]].every(Number.isFinite)&&d.reference_length_m[i]>0?(d.cp_x_m[i]-d.cg_x_m[i])/d.reference_length_m[i]:NaN)")
    payload=json.dumps(traces,allow_nan=False).replace("<","\\u003c")
    (out/"flight-viewer.html").write_text(template.replace("__DATA__",payload))


def paired_sensitivity(rows, out):
    """Rank association with design differences, not causal variance attribution."""
    stats=[]
    fig, axes=plt.subplots(3,2,figsize=(13,14))
    for col,motor in enumerate(("D12","E12")):
        groups=defaultdict(dict)
        for r in rows:
            if "master_seed" in r["inputs"] and r["design"] in (f"b500-n40-ogive-{motor}",f"b530-n40-ogive-{motor}"):
                groups[(r["inputs"]["master_seed"],r["inputs"]["index"])][r["design"][:4]]=r
        pairs=[g for g in groups.values() if "b500" in g and "b530" in g]
        fields=sorted({k for g in pairs for k in g["b500"]["inputs"] if k.startswith("mass:") or k in ("finish_g","wind_speed_m_s","shear_m_s","veer_deg","tilt_deg","turbulence_m_s")})
        for j,metric in enumerate(PAIRED):
            ranks=[]
            for field in fields:
                a=np.asarray([(g["b500"]["inputs"][field],value(g["b530"],metric)-value(g["b500"],metric)) for g in pairs if value(g["b500"],metric) is not None and value(g["b530"],metric) is not None])
                if len(a)>2 and np.ptp(a[:,0])>0 and np.ptp(a[:,1])>0:
                    rho=rank_correlation(a[:,0],a[:,1])
                    ranks.append((field,rho))
                    stats.append(dict(motor=motor,metric=metric,input=field,rho=rho,valid=len(a)))
            ranks.sort(key=lambda p:abs(p[1]))
            ax=axes[j,col]
            ax.barh([p[0] for p in ranks[-10:]],[p[1] for p in ranks[-10:]],color="#bd4374")
            ax.set(xlim=(-1,1),xlabel="Spearman rank correlation",title=f"{motor}: Δ {METRICS[metric]}")
    save(fig,out,"paired-sensitivity","What changes the design comparison? · 530 minus 500 mm ogive")
    return stats


def crosscheck_report(native_rows, folder, out):
    """Compare matched deterministic cases; shared drag is not independent CFD validation."""
    native={(r["design"],r["scenario"]):r for r in native_rows if r["phase"]=="deterministic" and r["inputs"]["turbulence_m_s"]==0}
    rows=[]; hashes={}
    for path in sorted(folder.glob("*.jsonl")):
        raw=path.read_bytes();hashes[str(path)]=hashlib.sha256(raw).hexdigest()
        rows.extend(json.loads(line) for line in raw.splitlines())
    keys=[(r["design"],r["scenario"]) for r in rows]
    if len(set(keys))!=len(keys):
        raise ValueError("Duplicate RocketPy design/scenario")
    if set(keys)-set(native):
        raise ValueError("RocketPy case lacks matching deterministic OpenRocket case")
    runtime_path=folder/"runtime.json"
    runtime=json.loads(runtime_path.read_text())
    hashes[str(runtime_path)]=hashlib.sha256(runtime_path.read_bytes()).hexdigest()
    result=dict(runtime=runtime,expected=len(native),recorded=len(rows),
                failed=sum(r["execution"]!="completed" for r in rows),
                warned=sum(bool(r.get("warnings")) for r in rows),not_recorded=len(native)-len(rows),metrics={})
    early=[dict(design=r["design"],scenario=r["scenario"]) for r in rows if r.get("planned_ejection_precedes_ballistic_apogee")]
    result["apogee_not_directly_comparable"]=early
    fig,axes=plt.subplots(2,2,figsize=(11,10))
    for ax,metric in zip(axes.flat,("apogee_m","guide_departure_m_s","powered_max_aoa_deg","burnout_tilt_deg")):
        result["metrics"][metric]=dict(valid=0,missing=len(native),median_delta=None,max_abs_delta=None)
        values=[]
        for motor,color in (("D12","#137eab"),("E12","#bd4374")):
            for base,marker in (("b500-n50-conical","s"),("b500-n40-ogive","o"),("b530-n40-ogive","^")):
                pairs=[(value(native[(r["design"],r["scenario"])],metric),value(r,metric)) for r in rows if r["design"]==f"{base}-{motor}" and not (metric=="apogee_m" and r.get("planned_ejection_precedes_ballistic_apogee"))]
                pairs=[p for p in pairs if None not in p]
                if pairs:
                    ax.scatter(*zip(*pairs),color=color,marker=marker,label=f"{base}-{motor}",alpha=.7,s=24)
                    values.extend(pairs)
        if values:
            a=np.asarray(values);lo=float(a.min());hi=float(a.max());ax.plot([lo,hi],[lo,hi],"k--",alpha=.4)
            result["metrics"][metric]=dict(valid=len(a),missing=len(native)-len(a),median_delta=float(np.median(a[:,1]-a[:,0])),max_abs_delta=float(np.max(np.abs(a[:,1]-a[:,0]))))
        result["metrics"][metric]["excluded_not_comparable"]=len(early) if metric=="apogee_m" else 0
        ax.set(xlabel="OpenRocket: "+METRICS[metric],ylabel="RocketPy: "+METRICS[metric])
        ax.grid(alpha=.2)
    if axes[0,0].get_legend_handles_labels()[0]:
        axes[0,0].legend(fontsize=6)
    axes[0,0].set_title(f"{len(early)} pre-apogee ejection cases excluded")
    save(fig,out,"rocketpy-crosscheck","Matched deterministic cross-check · shared drag, distinct normal-force models")
    (out/"rocketpy-summary.json").write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    return hashes


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, default=Path("docs/assets/flight-robustness"))
    p.add_argument("--rocketpy", type=Path, help="Optional completed RocketPy cross-check folder")
    p.add_argument("--require-complete",action="store_true",help="Reject unfinished campaigns before writing final assets")
    args = p.parse_args()
    study = json.loads((args.input/"study.json").read_text())
    if study["schema_version"] != 4:
        raise ValueError("Use final schema 4: isolated workfiles and explicitly seeded wind levels")
    rows, hashes, incomplete = load(args.input)
    verify_snapshot(args.input,study,rows,args.require_complete)
    args.output.mkdir(parents=True, exist_ok=True)
    convergence, sensitivity = render(rows, study, args.output)
    interactive(rows, args.output)
    pair_sensitivity=paired_sensitivity(rows,args.output)
    if args.rocketpy:
        hashes.update(crosscheck_report(rows,args.rocketpy,args.output))
    for name in ("long-guide-upper","verification"):
        folder=args.input/name
        if not (folder/"comparison.json").exists():
            continue
        evidence={}
        paths=[folder/"comparison.json",folder/"provenance.json"]+sorted(folder.glob("*-repeatability.json"))
        for path in paths:
            raw=path.read_bytes();hashes[str(path)]=hashlib.sha256(raw).hexdigest()
            evidence[path.name]=json.loads(raw)
        (args.output/f"{name}.json").write_text(json.dumps(evidence,indent=2,allow_nan=False)+"\n")
    groups = []
    imported = {r["scenario"] for r in rows if r["phase"]=="deterministic" and r["scenario"].startswith("imported-")}
    for phase in ["deterministic"] + [f"ensemble-{s}" for s in study["seeds"]]:
        for model in study["models"]:
            rr = [r for r in rows if r["phase"]==phase and r["design"]==model]
            expected = 20+len(imported) if phase == "deterministic" else study["samples_per_seed"]
            criteria=json.loads((args.input/model/"nominal.json").read_text())["criteria"]
            screens={}
            for c in criteria:
                if c["metric"] not in ("guide_departure_m_s","minimum_ascent_stability_cal","deployment_speed_m_s"):
                    continue
                for field,side in (("minimum","below"),("maximum","above")):
                    if c.get(field) is not None:
                        screens[f'{c["metric"]}_{side}_configured']=threshold_count(rr,c["metric"],c[field],side,expected)
            for threshold in (1.,1.5):
                screens[f"powered_stability_below_{threshold:g}"]=threshold_count(rr,"powered_min_stability_cal",threshold,"below",expected)
            groups.append(dict(phase=phase, design=model, expected=expected, recorded=len(rr),
                failed=sum(r["execution"]!="completed" for r in rr),
                incomplete_powered_data=sum(r.get("engine")=="OpenRocket" and not r.get("metrics",{}).get("powered_data_complete") for r in rr),
                warned=sum(bool(r.get("warnings")) for r in rr), not_recorded=max(0,expected-len(rr)),
                screens=screens,
                metrics={m:statistics([value(r,m) for r in rr], expected, bootstrap=200) for m in METRICS}))
    paired = {motor:{metric:statistics(paired_rows(rows,motor,metric), study["samples_per_seed"]*len(study["seeds"])) for metric in PAIRED} for motor in ("D12", "E12")}
    report = dict(scope=study["scope"], groups=groups, paired=paired, convergence=convergence, sensitivity=sensitivity, paired_sensitivity=pair_sensitivity, incomplete_lines=incomplete)
    (args.output/"summary.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    with (args.output/"flights.csv").open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=["phase","design","scenario","execution","warning_count","error",*METRICS])
        writer.writeheader()
        for row in rows:
            writer.writerow(dict({k:row.get(k) for k in ("phase","design","scenario","execution","error")},warning_count=len(row.get("warnings",[])),**{m:value(row,m) for m in METRICS}))
    for path in (args.input/"study.json", args.input/"samples.json", Path(__file__)):
        hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
    provenance = dict(source_files_sha256=hashes, study_sources=study["source_sha256"],
        output_files_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in args.output.iterdir() if p.is_file() and p.name!="provenance.json"})
    (args.output/"provenance.json").write_text(json.dumps(provenance, indent=2)+"\n")
    print(json.dumps(dict(recorded=len(rows), failed=sum(g["failed"] for g in groups), warned=sum(g["warned"] for g in groups), not_recorded=sum(g["not_recorded"] for g in groups))))


if __name__ == "__main__":
    main()
