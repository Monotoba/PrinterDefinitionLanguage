# Getting Started

## 1. Install the validator

```bash
git clone https://github.com/Monotoba/PrinterDefinitionLanguage.git
cd PrinterDefinitionLanguage
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

On Windows, activate the environment with `.venv\\Scripts\\activate`.

## 2. Create a definition

Start with this minimal YAML document:

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

Use a stable lowercase `vendor.model` identifier. Dimensions are millimetres
unless the specification explicitly says otherwise.

## 3. Validate it

```bash
python scripts/validate_examples.py my_printer.yaml
```

A successful run prints `Validated 1 PDL document(s).` and exits with status 0.

## 4. Add capabilities

Use the [full example](examples/full_lk5pro.yaml) and
[specification](PDL_SPEC.md) to add extruders, probe information, machine
limits, material ranges, process defaults, and G-code hooks.

## 5. Generate slicer profiles

[OpenPrintKit](https://github.com/Monotoba/OpenPrintKit) consumes PDL and can
generate profiles for OrcaSlicer, Cura, PrusaSlicer, and other targets.
