# Printer Definition Language (PDL)

[![Validate](https://github.com/Monotoba/PrinterDefinitionLanguage/actions/workflows/validate.yml/badge.svg)](https://github.com/Monotoba/PrinterDefinitionLanguage/actions/workflows/validate.yml)
[![Documentation](https://github.com/Monotoba/PrinterDefinitionLanguage/actions/workflows/docs.yml/badge.svg)](https://github.com/Monotoba/PrinterDefinitionLanguage/actions/workflows/docs.yml)
[![PDL 1.0](https://img.shields.io/badge/PDL-1.0-2C7A7B)](docs/PDL_SPEC.md)
[![JSON Schema 2020-12](https://img.shields.io/badge/JSON%20Schema-2020--12-005A9C?logo=json)](schemas/pdl.schema.json)
[![License: BSD-2-Clause](https://img.shields.io/badge/License-BSD--2--Clause-blue.svg)](LICENSE)

PDL is an open, slicer-agnostic format for describing 3D printers, materials,
process defaults, machine capabilities, and reusable G-code hooks in YAML or
JSON. A single validated definition can serve as the source for profiles in
multiple slicers.

## Why PDL?

- **Portable:** describe hardware and print defaults independently of one slicer.
- **Reviewable:** keep printer profiles as readable, version-controlled text.
- **Validatable:** catch structural errors with the included JSON Schema.
- **Extensible:** model multiple extruders, material systems, probes, and custom hooks.
- **Reproducible:** generate slicer profiles from the same canonical definition.

## Minimal example

```yaml
pdl_version: 1.0.0
id: vendor.model
name: Vendor Model
firmware: marlin
kinematics: cartesian
geometry:
  bed_shape: [[0, 0], [220, 0], [220, 220], [0, 220]]
  z_height: 250
```

## Validate a definition

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python scripts/validate_examples.py
```

Validate one file:

```bash
python scripts/validate_examples.py path/to/printer.yaml
```

## Repository contents

- [`schemas/pdl.schema.json`](schemas/pdl.schema.json) — canonical JSON Schema
- [`docs/PDL_SPEC.md`](docs/PDL_SPEC.md) — PDL 1.0 draft specification
- [`examples/`](examples/) — complete example definitions
- [`docs/getting-started.md`](docs/getting-started.md) — authoring guide
- [`OpenPrintKit`](https://github.com/Monotoba/OpenPrintKit) — reference tooling and slicer generators

## Project status

PDL 1.0 is a **draft specification**. Feedback, example printer definitions,
and compatibility reports are welcome. Schema changes follow semantic
versioning: major versions may break compatibility, minor versions add
backward-compatible fields, and patch versions clarify or correct the spec.

See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing schema changes.

## License

BSD-2-Clause. See [LICENSE](LICENSE).
