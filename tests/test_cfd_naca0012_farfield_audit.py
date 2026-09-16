import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_naca0012_farfield_audit import (  # noqa: E402
    patch_values,
    segment_labels,
    transport_statistics,
)
from cfd_naca0012_surface_force_audit import (  # noqa: E402
    final_logged_components,
    internal_scalar,
    internal_vector,
)
from cfd_naca0012_gradient_audit import (  # noqa: E402
    distribution,
    internal_tensor,
)
from cfd_naca0012_skin_friction_localization import (  # noqa: E402
    BINS,
    localize,
)


def test_patch_values_reads_scalar_and_vector_nonuniform_lists(tmp_path):
    scalar = tmp_path / "p"
    scalar.write_text(
        "boundaryField\n{\nfarfield\n{\ntype calculated;\n"
        "value nonuniform List<scalar> 2\n(\n1\n2\n)\n;\n}\n}\n"
    )
    vector = tmp_path / "U"
    vector.write_text(
        "boundaryField\n{\nfarfield\n{\ntype calculated;\n"
        "value nonuniform List<vector> 2\n(\n(1 2 3)\n(4 5 6)\n)\n;\n}\n}\n"
    )
    np.testing.assert_allclose(patch_values(scalar, "farfield", 2), [1, 2])
    np.testing.assert_allclose(
        patch_values(vector, "farfield", 2), [[1, 2, 3], [4, 5, 6]]
    )


def test_segment_labels_uses_oriented_dominant_normal():
    vectors = np.asarray(
        [
            [-2.0, 0.1, 0.0],
            [0.1, 2.0, 0.0],
            [0.1, -2.0, 0.0],
            [2.0, 0.1, 0.0],
        ]
    )
    assert segment_labels(vectors).tolist() == [
        "upstream",
        "upper",
        "lower",
        "downstream",
    ]


def test_transport_statistics_reports_closed_uniform_transport():
    mask = np.ones(4, dtype=bool)
    phi = np.asarray([-2.0, 1.0, 0.5, 0.5])
    velocity = np.repeat([[3.0, 0.0, 0.0]], 4, axis=0)
    pressure = np.full(4, 101325.0)
    temperature = np.full(4, 300.0)
    area_vectors = np.asarray(
        [[-1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, -1.0, 0.0]]
    )
    result = transport_statistics(
        mask,
        phi,
        velocity,
        pressure,
        temperature,
        area_vectors,
        101325.0,
        1004.5,
    )
    assert result["mass_flux"]["net_outward"] == 0.0
    assert result["mass_flux"]["absolute_closure_over_total_throughflow"] == 0.0
    np.testing.assert_allclose(result["convective_plus_pressure_momentum_flux_outward"], 0.0)
    assert result["convective_total_enthalpy_flux_outward"] == 0.0
    assert result["absolute_energy_closure_over_total_transport"] == 0.0


def test_surface_force_helpers_parse_internal_pressure_and_final_log(tmp_path):
    pressure = tmp_path / "p"
    pressure.write_text(
        "internalField nonuniform List<scalar> 3\n(\n101324\n101325\n101326\n)\n;\n"
    )
    np.testing.assert_allclose(internal_scalar(pressure), [101324, 101325, 101326])

    velocity = tmp_path / "U"
    velocity.write_text(
        "internalField nonuniform List<vector> 2\n(\n(1 2 3)\n(4 5 6)\n)\n;\n"
    )
    np.testing.assert_allclose(internal_vector(velocity), [[1, 2, 3], [4, 5, 6]])

    log = tmp_path / "solver.log"
    log.write_text(
        "Cd: 0.1 0.02 0.08 0\n"
        "Cd: 0.2 0.03 0.17 0\n"
    )
    assert final_logged_components(log, "Cd") == {
        "total": 0.2,
        "pressure": 0.03,
        "viscous": 0.17,
        "internal": 0.0,
    }


def test_gradient_audit_parses_tensors_and_summarizes_distribution(tmp_path):
    gradient = tmp_path / "grad(U)"
    gradient.write_text(
        "internalField nonuniform List<tensor> 2\n(\n"
        "(1 2 3 4 5 6 7 8 9)\n"
        "(9 8 7 6 5 4 3 2 1)\n"
        ")\n;\n"
    )
    values = internal_tensor(gradient)
    assert values.shape == (2, 3, 3)
    np.testing.assert_allclose(values[0], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert distribution(np.asarray([1.0, 3.0]))["mean"] == 2.0


def test_skin_friction_localization_uses_fixed_chord_bins(tmp_path):
    plan = tmp_path / "plan.json"
    plan.write_text('{"declared_before_new_solver_execution": true}')
    profile = []
    for index, (lower, upper) in enumerate(BINS):
        profile.append(
            {
                "x_over_c": (lower + upper) / 2,
                "openfoam_cf": 1.0 + index / 10,
                "cfl3d_cf": 1.0,
            }
        )
    audit = tmp_path / "skin.json"
    audit.write_text(json.dumps({"profile": profile}))
    result = localize(plan, audit)
    assert len(result["bins"]) == len(BINS)
    assert result["downstream_bin_means_strictly_increase"] is True
