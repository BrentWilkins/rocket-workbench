"""Repair unescaped compatible-printer quotes emitted by Bambu Studio CLI.

Some Linux AppImage CLI exports write an XML attribute such as
``value=""Bambu ...";"Bambu ...""``.  That is not well-formed XML, and the
decoded value is not accepted by the desktop application either. This tool
preserves all archive members and removes only those malformed list-valued
per-object overrides; project-level printer and filament settings remain.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def repair(text: str) -> str:
    lines = []
    count = 0
    for line in text.splitlines(keepends=True):
        marker = ' value=""'
        if marker in line and line.rstrip().endswith('"/>'):
            prefix, payload = line.split(' value=', 1)
            # These values were produced from vector settings (for example,
            # compatible_printers) in a form neither XML nor Bambu accepts.
            # Drop the per-object override; project-level settings remain.
            line = ""
            count += 1
        lines.append(line)
    result = ''.join(lines)
    if count == 0:
        raise ValueError("No malformed list-valued metadata found")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    with ZipFile(args.source) as source:
        members = {name: source.read(name) for name in source.namelist()}
    name = "Metadata/model_settings.config"
    if name not in members:
        raise ValueError(f"Missing {name}")
    members[name] = repair(members[name].decode()).encode()
    with ZipFile(args.output, "x", ZIP_DEFLATED) as output:
        for member, payload in members.items():
            output.writestr(member, payload)


if __name__ == "__main__":
    main()
