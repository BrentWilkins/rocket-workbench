"""Emit a checked transcription of matched NASA TM-4074 force tables."""

import argparse
import hashlib
import json
from pathlib import Path


PDF_SHA256 = "8e466706cbdf54b3c778ea2b089c4f52d87686bf7f6b1bd10d224b42c2d06902"
OUTPUT_NAME = "ladson-m015-r6-tripped-force-table.json"

# Values are transcribed from the R approximately 6 million blocks of NASA
# TM-4074 Tables IX and XI. The printed and PDF page numbers make the manual
# transcription auditable without treating OCR output as authoritative.
ROWS = (
    {
        "table": "IX",
        "printed_page": 19,
        "pdf_page": 21,
        "grit": "80-W",
        "reynolds_number_chord": 5_950_000,
        "alpha_deg": -0.05,
        "cd": 0.00809,
        "cl": -0.0126,
        "cm_quarter_chord_nose_up": 0.0001,
    },
    {
        "table": "IX",
        "printed_page": 19,
        "pdf_page": 21,
        "grit": "80-W",
        "reynolds_number_chord": 5_950_000,
        "alpha_deg": 10.12,
        "cd": 0.01201,
        "cl": 1.0707,
        "cm_quarter_chord_nose_up": 0.0052,
    },
    {
        "table": "XI",
        "printed_page": 21,
        "pdf_page": 23,
        "grit": "120",
        "reynolds_number_chord": 6_000_000,
        "alpha_deg": -0.01,
        "cd": 0.00811,
        "cl": -0.0120,
        "cm_quarter_chord_nose_up": 0.0001,
    },
    {
        "table": "XI",
        "printed_page": 21,
        "pdf_page": 23,
        "grit": "120",
        "reynolds_number_chord": 6_000_000,
        "alpha_deg": 0.01,
        "cd": 0.00804,
        "cl": -0.0122,
        "cm_quarter_chord_nose_up": 0.0008,
    },
    {
        "table": "XI",
        "printed_page": 21,
        "pdf_page": 23,
        "grit": "120",
        "reynolds_number_chord": 6_000_000,
        "alpha_deg": 10.10,
        "cd": 0.01175,
        "cl": 1.0775,
        "cm_quarter_chord_nose_up": 0.0049,
    },
)


def matched_rows(angle_deg: float) -> list[dict]:
    return [dict(row) for row in ROWS if abs(row["alpha_deg"] - angle_deg) <= 0.2]


def emit(source_pdf: Path, output: Path) -> dict:
    digest = hashlib.sha256(source_pdf.read_bytes()).hexdigest()
    if digest != PDF_SHA256:
        raise ValueError(f"NASA TM-4074 SHA-256 mismatch: {digest}")
    output.mkdir(parents=True, exist_ok=True)
    target = output / OUTPUT_NAME
    if target.exists():
        raise FileExistsError(target)
    result = {
        "source": {
            "title": "NASA TM-4074",
            "url": "https://ntrs.nasa.gov/citations/19880019495",
            "file": str(source_pdf),
            "sha256": digest,
        },
        "conditions": {
            "mach": 0.15,
            "transition": "fixed with grit",
            "target_reynolds_number_chord": 6_000_000,
            "maximum_relative_reynolds_difference": 0.01,
        },
        "method": "manual transcription from printed tables; PDF page images visually checked",
        "rows": list(ROWS),
        "accepted_for_rocket": False,
    }
    target.write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-pdf", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(emit(args.source_pdf, args.output)))


if __name__ == "__main__":
    main()
