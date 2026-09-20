# Separate collar and fin for manual assembly

This option has two print geometries:

- [Round collar STL](assets/separate-fin-collar-v1/round-collar.stl) — print **one**, aft end on the bed.
- [Single fin STL](assets/separate-fin-collar-v1/single-fin.stl) — print **three**, each flat on a broad side.

The [Bambu Studio project](assets/separate-fin-collar-v1/separate-collar-three-fins.3mf) contains those four print
objects on one plate. The [sliced project](assets/separate-fin-collar-v1/separate-collar-three-fins-sliced.3mf) is for
toolpath review. It sliced locally on X1C/0.4 mm with Generic PLA and 0.20 mm layers, with no support extrusion in the
G-code. It was not sent to a printer.

The [assembled STEP](assets/separate-fin-collar-v1/assembled-fit-reference.step) shows the three fins spaced 120 degrees
apart. It is **only a fit reference**; it is not a single printable part. The
[collar STEP](assets/separate-fin-collar-v1/round-collar.step) and
[fin STEP](assets/separate-fin-collar-v1/single-fin.step) are separate CAD solids. The
[summary](assets/separate-fin-collar-v1/summary.json) lists sizes and quantities; the
[manifest](assets/separate-fin-collar-v1/manifest.json) records file hashes.

The collar is plain and round, with a 44.4 mm outside diameter, 42.0 mm bore, and 65 mm straight section. The fin is a
plain 2.0 mm thick clipped delta with 63 mm of root contact and 53.65 mm span. There are no integrated fins, root
fillets, sockets, or trailing/tip tapers. The fin root begins 2 mm below the forward collar rim and reaches the aft
collar edge, so the aft edge can sit on the bed when the collar is printed. The collar's 1.2 mm wall remains uncut.

Dry fit the collar to the tube, mark three positions 120 degrees apart, and dry fit the fins before bonding. Add the
root fillets manually after the fins are attached. The adhesive and fillets form the joint; their strength, the finished
mass, and flight performance have not been validated. Weigh the finished part and update the flight model before
treating it as a flight part.

Regenerate the files with:

```bash
PYTHONPATH=src:. .venv/bin/python scripts/prepare_separate_fin_collar.py \
  --output /tmp/separate-fin-collar-regenerated
```
