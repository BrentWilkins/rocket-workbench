# Third-party sources and licenses

Inventory checked 2026-09-12 against installed package metadata and upstream
sources. This is an attribution/dependency inventory, not legal advice or a
redistribution clearance. No binaries are published by this task. Retain bundled
notices and review their full terms before distributing software or artifacts.

| Component    | Tested identity                                                          | Source / license information                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Python       | 3.14.6                                                                   | [Python](https://www.python.org/), PSF license and bundled notices                                                                                                                                      |
| uv           | 0.11.17                                                                  | [Astral uv](https://github.com/astral-sh/uv), MIT / Apache-2.0                                                                                                                                          |
| OpenRocket   | 24.12                                                                    | [Release](https://github.com/openrocket/openrocket/releases/tag/release-24.12), [GPLv3 license](https://github.com/openrocket/openrocket/blob/release-24.12/LICENSE.TXT)                                |
| orhelper     | fork revision `fb132c49e661bb00c5586cce6a4ac0c655425197`; metadata 0.1.5 | [Pinned source and LICENSE](https://github.com/openrocket/orhelper/tree/fb132c49e661bb00c5586cce6a4ac0c655425197), GPLv2; no local patch                                                                |
| Java         | Oracle JDK 21.0.3+7-LTS-152                                              | Existing local installation; [Oracle JDK terms](https://www.oracle.com/java/technologies/javase/jdk-faqs.html). Not redistributed; another JDK needs acceptance testing                                 |
| CadQuery     | 2.8.0                                                                    | [Source](https://github.com/CadQuery/cadquery), Apache-2.0                                                                                                                                              |
| cadquery-ocp | 7.9.3.1.1                                                                | [Bindings](https://github.com/CadQuery/OCP), Apache-2.0 metadata; underlying [Open CASCADE](https://dev.opencascade.org/resources/licensing) has separate LGPL/exception terms and bundled dependencies |
| JPype1       | 1.7.1                                                                    | [Source](https://github.com/jpype-project/jpype), Apache-2.0                                                                                                                                            |
| NumPy        | 2.5.3                                                                    | [Source](https://github.com/numpy/numpy); installed expression BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0                                                                                       |
| Pydantic     | 2.13.5                                                                   | [Source](https://github.com/pydantic/pydantic), MIT                                                                                                                                                     |
| PyYAML       | 6.0.3                                                                    | [Source](https://github.com/yaml/pyyaml), MIT                                                                                                                                                           |
| pytest       | 9.1.1                                                                    | [Source](https://github.com/pytest-dev/pytest), MIT                                                                                                                                                     |

`uv.lock` records all transitive packages and hashes; this table is not a full
transitive-license audit. The JAR checksum is
`4959b72f52f5f607941e9722abbb7b7f0c4a38ebbbf84204a329db9f31c4f897`.

The unchanged `examples/upstream-simple.ork` is the reference from the pinned
orhelper examples, attributed in the file to Sampo Niskanen. It is not our
original rocket design. Its SHA256 is
`f5f4de21acd2279895dfb7376c3353fd4e643b85adbcd034808b1af48f439c21`.
Motor curves are the data bundled with the pinned OpenRocket engine; exact
curve identity, attribution/description and sampled data are retained in the
results. Manufacturer retail specifications are separately linked from inputs.
