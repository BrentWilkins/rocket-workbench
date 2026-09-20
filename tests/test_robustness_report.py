import importlib.util
import hashlib
import json
from pathlib import Path
import sys

import pytest

spec = importlib.util.spec_from_file_location("plot_robustness", Path(__file__).parents[1]/"scripts/plot_robustness.py")
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)


def row(body, seed, index, result=1, status="completed"):
    return dict(design=f"b{body}-n40-ogive-E12", inputs=dict(master_seed=seed,index=index),
                metrics=dict(apogee_m=result), execution=status)


def test_pairs_preserve_identity_and_missingness():
    rows=[row(500,1,0,10),row(530,1,0,8),row(500,2,0,11),row(530,2,0,5),
          row(500,1,1,12),row(530,1,1,0,"failed"),row(500,1,2,13)]
    assert report.paired_rows(rows,"E12","apogee_m")==[-2,None,None,-6]
    assert report.paired_rows(rows,"E12","apogee_m",1,1)==[-2]


def test_statistics_counts_absent_and_invalid():
    s=report.statistics([1,2,3,None,float("nan")],expected=8,bootstrap=20)
    assert (s["expected"],s["valid"],s["missing"])==(8,3,5)
    assert s["quantiles"][1]==2
    assert s==report.statistics([1,2,3,None],expected=8,bootstrap=20)
    assert report.statistics([],3)["ci95"] is None
    with pytest.raises(ValueError,match="denominator"):
        report.statistics([1,2,3],expected=2)


def test_threshold_counts_do_not_turn_missing_into_passes():
    rows=[row(500,1,0,9),row(500,1,1,10),row(500,1,2,11),row(500,1,3,99,"failed")]
    s=report.threshold_count(rows,"apogee_m",10,"above",7)
    assert (s["beyond"],s["valid"],s["missing"],s["expected"])==(1,3,4,7)
    assert s["fraction_of_valid"]==1/3


def test_rank_correlation_handles_ties():
    assert report.rank_correlation([1,1,3,4],[4,4,2,1])==pytest.approx(-1)
    assert report.rank_correlation([1,2,3],[2,6,18])==pytest.approx(1)


def test_incomplete_native_thrust_invalidates_powered_metrics():
    r=dict(engine="OpenRocket",execution="completed",metrics=dict(powered_min_stability_cal=2,powered_data_complete=False,apogee_m=100))
    assert report.value(r,"powered_min_stability_cal") is None
    assert report.value(r,"apogee_m")==100
    del r["metrics"]["powered_data_complete"]
    assert report.value(r,"powered_min_stability_cal") is None
    r["metrics"]["powered_data_complete"]=True
    assert report.value(r,"powered_min_stability_cal")==2


def test_load_partial_tail_and_duplicate_detection(tmp_path):
    folder=tmp_path/"deterministic";folder.mkdir()
    path=folder/"a.jsonl"
    r=dict(phase="deterministic",design="a",scenario="b")
    path.write_text(json.dumps(r)+'\n{"incomplete":')
    rows,hashes,partial=report.load(tmp_path)
    assert len(rows)==1 and partial==[str(path)] and str(path) in hashes
    path.write_text((json.dumps(r)+'\n')*2)
    with pytest.raises(ValueError,match="Duplicate"):
        report.load(tmp_path)


def test_viewer_preserves_missing_channels_and_equal_trajectory_scale(tmp_path):
    channels=("time_s","east_m","north_m","altitude_m","orientation_theta_rad","angle_of_attack_rad","cp_x_m","cg_x_m","reference_length_m")
    r=dict(design="b500-n40-ogive-E12",scenario="example",phase="deterministic",
           timeseries={k:[0,None,1] for k in channels})
    report.interactive([r],tmp_path)
    html=(tmp_path/"flight-viewer.html").read_text()
    assert "every(Number.isFinite)" in html
    assert "Number.isFinite(d.angle_of_attack_rad[i])" in html
    assert "w*530/1080" in html
    assert "const traces=" in html


def test_crosscheck_counts_failures_and_rejects_unmatched(tmp_path,monkeypatch):
    native=[dict(design="b500-n40-ogive-E12",scenario="calm",phase="deterministic",
                 execution="completed",inputs=dict(turbulence_m_s=0),metrics=dict(apogee_m=100))]
    folder=tmp_path/"rp";folder.mkdir()
    (folder/"runtime.json").write_text('{}')
    path=folder/"test.jsonl"
    failed=dict(design="b500-n40-ogive-E12",scenario="calm",execution="simulation failed",metrics={})
    path.write_text(json.dumps(failed)+'\n')
    monkeypatch.setattr(report,"save",lambda fig,*args:report.plt.close(fig))
    report.crosscheck_report(native,folder,tmp_path)
    summary=json.loads((tmp_path/"rocketpy-summary.json").read_text())
    assert summary["failed"]==1 and summary["expected"]==1
    assert summary["metrics"]["apogee_m"]["missing"]==1
    early={**failed,"execution":"completed","metrics":{"apogee_m":101},"planned_ejection_precedes_ballistic_apogee":True}
    path.write_text(json.dumps(early)+'\n')
    report.crosscheck_report(native,folder,tmp_path)
    summary=json.loads((tmp_path/"rocketpy-summary.json").read_text())
    assert summary["failed"]==0
    assert summary["metrics"]["apogee_m"]["valid"]==0
    assert summary["metrics"]["apogee_m"]["excluded_not_comparable"]==1
    failed["scenario"]="unmatched"
    path.write_text(json.dumps(failed)+'\n')
    with pytest.raises(ValueError,match="lacks matching"):
        report.crosscheck_report(native,folder,tmp_path)


@pytest.mark.parametrize("schema",[1,2,3])
def test_reject_unseeded_or_uncorrected_studies(tmp_path,monkeypatch,schema):
    (tmp_path/"study.json").write_text(json.dumps(dict(schema_version=schema)))
    monkeypatch.setattr(sys,"argv",["plot_robustness.py","--input",str(tmp_path)])
    with pytest.raises(ValueError,match="schema 4"):
        report.main()


def test_snapshot_requires_exact_shared_inputs_and_complete_coverage(tmp_path):
    sample=dict(id="s1",master_seed=1,index=0,finish_g=2)
    raw=json.dumps([sample]).encode();(tmp_path/"samples.json").write_bytes(raw)
    study=dict(samples_sha256=hashlib.sha256(raw).hexdigest(),models=["a"])
    row=dict(phase="ensemble-1",design="a",scenario="s1",inputs=sample)
    report.verify_snapshot(tmp_path,study,[row])
    with pytest.raises(ValueError,match="missing 1"):
        report.verify_snapshot(tmp_path,study,[],True)
    with pytest.raises(ValueError,match="shared sample"):
        report.verify_snapshot(tmp_path,study,[{**row,"inputs":{**sample,"finish_g":3}}])
