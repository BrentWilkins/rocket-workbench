import json
from pathlib import Path


def test_validation_plan_fails_closed_and_predeclares_benchmarks():
    plan=json.loads((Path(__file__).parents[1]/'cfd'/'validation-plan.json').read_text())
    assert plan['overall_status'] == 'not_validated'
    assert len(plan['benchmarks']) >= 2
    statuses={benchmark['id']:benchmark['status'] for benchmark in plan['benchmarks']}
    assert statuses['tmr-2dzp-flat-plate'] == (
        'accepted_attached_wall_sstm_subsystem_only'
    )
    assert statuses['tmr-naca0012-external-body'] == (
        'exact_model_grid_scheme_wall_recovered_reduced_domain_residual_gate_failed_zero_angle_benchmark_failed'
    )
    assert all('predeclared_tolerance' in benchmark for benchmark in plan['benchmarks'])
    gates={entry['gate']:entry['status'] for entry in plan['acceptance_matrix']}
    assert gates['conventional_rocket_cross_model'] == 'blocked_by_prior_gates'
    assert gates['novel_fin_ranking'] == 'blocked_by_prior_gates'


def test_gate3_remediation_plan_preserves_thresholds_and_downstream_block():
    plan = json.loads(
        (
            Path(__file__).parents[1]
            / "cfd"
            / "naca0012-gate3-remediation-plan.json"
        ).read_text()
    )
    assert plan["declared_before_new_solver_execution"] is True
    assert plan["fixed_configuration"]["runtime_model"] == "TmrSSTmExactProduction"
    assert plan["fixed_configuration"]["mpi_ranks"] == 12
    assert plan["fixed_configuration"]["gpu"] is False
    assert plan["phase_order"][1]["candidates"]["250c"]["iterations"] == 4000
    assert plan["phase_order"][1]["candidates"]["150c"]["iterations"] == 4000
    assert "cannot replace" in plan["terminal_rules"]["domain_non_substitution"]
    assert "Do not run" in plan["terminal_rules"]["downstream_block"]


def test_exact_wall_distance_sensitivity_is_single_change_and_fail_closed():
    plan = json.loads(
        (
            Path(__file__).parents[1]
            / "cfd"
            / "naca0012-exact-wall-distance-sensitivity-plan.json"
        ).read_text()
    )
    assert plan["declared_before_candidate_execution"] is True
    assert plan["candidate"]["single_change"] == (
        "Replace wallDist method meshWave with exact."
    )
    assert plan["candidate"]["same_boundary_conditions"] is True
    assert plan["candidate"]["iterations"] == 2000
    assert plan["mechanism_test"][
        "minimum_cd_change_beyond_existing_numerical_variation"
    ] == 0.00003368094464354697
    assert plan["no_post_hoc_threshold_changes"] is True
