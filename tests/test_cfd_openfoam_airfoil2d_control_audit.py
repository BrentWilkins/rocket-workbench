import gzip
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_openfoam_airfoil2d_control_audit import (
    input_integrity,
    parse_foam_list_count,
    parse_patch_faces,
    parse_scalar,
    parse_uniform_vector,
    solver_completion,
)


def test_control_input_integrity_detects_changed_file(tmp_path):
    pristine = tmp_path / "pristine"
    case = tmp_path / "case"
    pristine.mkdir()
    case.mkdir()
    (pristine / "input").write_text("official\n")
    (case / "input").write_text("official\n")
    _, matches = input_integrity(pristine, case)
    assert matches

    (case / "input").write_text("changed\n")
    records, matches = input_integrity(pristine, case)
    assert not matches
    assert records[0]["matches"] is False


def test_control_parsers_read_openfoam_values(tmp_path):
    field = tmp_path / "U"
    field.write_text("internalField uniform (25.75 3.62 0);\n")
    transport = tmp_path / "transportProperties"
    transport.write_text("nu [0 2 -1 0 0 0 0] 1e-05;\n")
    assert parse_uniform_vector(field, "internalField") == [25.75, 3.62, 0.0]
    assert parse_scalar(transport, "nu") == 1e-5


def test_control_parsers_read_compressed_mesh_metadata(tmp_path):
    cells = tmp_path / "cells.gz"
    with gzip.open(cells, "wt") as stream:
        stream.write("FoamFile {}\n10720\n(\n)\n")
    boundary = tmp_path / "boundary.gz"
    with gzip.open(boundary, "wt") as stream:
        stream.write("FoamFile {}\n1\n(\nwalls\n{\nnFaces 78;\n}\n)\n")
    assert parse_foam_list_count(cells) == 10720
    assert parse_patch_faces(boundary, "walls") == 78


def test_solver_completion_rejects_masked_mpi_failure(tmp_path):
    solver = tmp_path / "log.simpleFoam"
    reconstruction = tmp_path / "log.reconstructPar"
    solver.write_text("mpirun has detected an attempt to run as root\n")
    reconstruction.write_text("No times selected\n")
    assert not solver_completion(solver, reconstruction)["passed"]

    solver.write_text("SIMPLE solution converged in 308 iterations\n")
    reconstruction.write_text("Time = 308\nEnd\n")
    result = solver_completion(solver, reconstruction)
    assert result["passed"]
    assert result["converged_iteration"] == 308
