"""Create a same-grid NACA restart with Sutherland viscosity and constant Pr."""

import argparse
import hashlib
import json
import shutil
from pathlib import Path

import numpy as np

from cfd_naca0012_map_fields import FIELDS, latest_time


METHOD = "same-grid polynomial-Sutherland constant-Prandtl sensitivity restart"
FIT_TEMPERATURE_RANGE_K = (250.0, 350.0)
FIT_DEGREE = 5
POLYNOMIAL_SIZE = 8
MOLECULAR_PRANDTL = 0.72
SPECIFIC_HEAT_CP = 1004.5
MAXIMUM_RELATIVE_VISCOSITY_FIT_ERROR = 2.0e-9


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one occurrence of {old!r}")
    return text.replace(old, new)


def transport_coefficients(
    sutherland_as: float, sutherland_temperature: float, cp: float
) -> tuple[list[float], list[float], float]:
    fit_temperature = np.linspace(*FIT_TEMPERATURE_RANGE_K, 401)
    fit_viscosity = (
        sutherland_as
        * np.sqrt(fit_temperature)
        / (1.0 + sutherland_temperature / fit_temperature)
    )
    polynomial = np.polynomial.Polynomial.fit(
        fit_temperature,
        fit_viscosity,
        FIT_DEGREE,
        domain=FIT_TEMPERATURE_RANGE_K,
    ).convert()
    mu_coefficients = np.pad(
        polynomial.coef, (0, POLYNOMIAL_SIZE - len(polynomial.coef))
    )
    verification_temperature = np.linspace(*FIT_TEMPERATURE_RANGE_K, 4001)
    exact_viscosity = (
        sutherland_as
        * np.sqrt(verification_temperature)
        / (1.0 + sutherland_temperature / verification_temperature)
    )
    fitted_viscosity = np.polynomial.polynomial.polyval(
        verification_temperature, mu_coefficients
    )
    maximum_relative_error = float(
        np.max(np.abs(fitted_viscosity / exact_viscosity - 1.0))
    )
    if maximum_relative_error > MAXIMUM_RELATIVE_VISCOSITY_FIT_ERROR:
        raise ValueError(
            f"Sutherland polynomial fit error {maximum_relative_error} exceeds limit"
        )
    kappa_coefficients = mu_coefficients * cp / MOLECULAR_PRANDTL
    return (
        [float(value) for value in mu_coefficients],
        [float(value) for value in kappa_coefficients],
        maximum_relative_error,
    )


def coefficient_list(values: list[float]) -> str:
    return "(" + " ".join(f"{value:.17g}" for value in values) + ")"


def restart(
    source: Path,
    source_audit: Path,
    target: Path,
    iterations: int,
) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)
    if iterations < 500:
        raise ValueError("At least 500 iterations are required for the trend gate")

    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    audit = json.loads(source_audit.read_text())
    execution = json.loads((source / "execution.json").read_text())
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source execution did not pass")
    if (
        Path(audit.get("case", "")).resolve() != source
        or not audit.get("coarse_preflight_passed")
        or not audit.get("solver_residual_gate")
        or not audit.get("long_window_trend_gate")
    ):
        raise ValueError("Source force audit did not pass")
    conditions = source_spec.get("conditions", {})
    if conditions.get("transport_model") != "sutherland":
        raise ValueError("Source must use built-in Sutherland transport")

    cp = SPECIFIC_HEAT_CP
    sutherland_as = float(conditions["sutherland_as"])
    sutherland_temperature = float(conditions["sutherland_temperature_k"])
    mu_coefficients, kappa_coefficients, fit_error = transport_coefficients(
        sutherland_as, sutherland_temperature, cp
    )

    target.mkdir(parents=True)
    shutil.copytree(source / "constant", target / "constant")
    shutil.copytree(source / "system", target / "system")
    shutil.copyfile(source / "tmr-naca0012-grid.npz", target / "tmr-naca0012-grid.npz")

    source_time = latest_time(source)
    initial = target / "0"
    initial.mkdir()
    fields = {}
    for name in FIELDS:
        source_field = source_time / name
        target_field = initial / name
        shutil.copyfile(source_field, target_field)
        fields[name] = {
            "source_sha256": sha256(source_field),
            "restart_sha256": sha256(target_field),
        }

    thermo_path = target / "constant" / "thermophysicalProperties"
    thermo = thermo_path.read_text()
    thermo = replace_once(thermo, "transport sutherland;", "transport polynomial;")
    thermo = replace_once(thermo, "thermo hConst;", "thermo hPolynomial;")
    thermo = replace_once(
        thermo,
        f" Cp {cp:.15g};\n Hf 0;",
        f" Hf 0;\n Sf 0;\n CpCoeffs<8> {coefficient_list([cp] + [0.0] * 7)};",
    )
    thermo = replace_once(
        thermo,
        f" As {sutherland_as:.15g};\n Ts {sutherland_temperature:.15g};",
        f" muCoeffs<8> {coefficient_list(mu_coefficients)};\n"
        f" kappaCoeffs<8> {coefficient_list(kappa_coefficients)};",
    )
    thermo_path.write_text(thermo)

    control_path = target / "system" / "controlDict"
    control = control_path.read_text()
    control = replace_once(control, "endTime 6000;", f"endTime {iterations};")
    control_path.write_text(control)

    provenance = target / "provenance"
    provenance.mkdir()
    implementation_snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), implementation_snapshot)
    implementation_sha256 = sha256(implementation_snapshot)

    initialization = {
        "method": METHOD,
        "stage_passed": True,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(implementation_snapshot),
        "implementation_sha256": implementation_sha256,
        "fields": fields,
    }
    spec = dict(source_spec)
    spec["iterations"] = iterations
    spec["conditions"] = dict(conditions)
    spec["conditions"].update(
        {
            "transport_model": "polynomial-sutherland-pr072",
            "openfoam_transport_model": "polynomial",
            "molecular_prandtl": MOLECULAR_PRANDTL,
        }
    )
    spec["transport_mapping"] = {
        "method": METHOD,
        "source_transport": "OpenFOAM sutherland",
        "target_transport": "OpenFOAM polynomial",
        "thermodynamics": "hPolynomial with constant Cp coefficient",
        "viscosity_law": "degree-5 polynomial fit to source Sutherland law",
        "fit_temperature_range_k": list(FIT_TEMPERATURE_RANGE_K),
        "maximum_relative_viscosity_fit_error": fit_error,
        "maximum_relative_viscosity_fit_error_limit": MAXIMUM_RELATIVE_VISCOSITY_FIT_ERROR,
        "molecular_prandtl": MOLECULAR_PRANDTL,
        "thermal_conductivity_relation": "kappa(T) = Cp * mu(T) / Pr",
        "mu_coefficients": mu_coefficients,
        "kappa_coefficients": kappa_coefficients,
    }
    spec["initialization"] = initialization
    spec_path = target / "benchmark-spec.json"
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")
    record = {
        "stage": METHOD,
        "stage_passed": True,
        **initialization,
        "target_case": str(target),
        "target_case_spec_sha256": sha256(spec_path),
        "target_thermophysical_properties_sha256": sha256(thermo_path),
    }
    (target / "transport-restart-execution.json").write_text(
        json.dumps(record, indent=2) + "\n"
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--iterations", type=int, default=1500)
    args = parser.parse_args()
    print(json.dumps(restart(args.source, args.source_audit, args.target, args.iterations)))


if __name__ == "__main__":
    main()
