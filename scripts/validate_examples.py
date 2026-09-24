#!/usr/bin/env python3
"""Validate PDL YAML or JSON documents against the canonical schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "pdl.schema.json"
DEFAULT_PATTERNS = (
    "examples/*.yaml",
    "examples/*.yml",
    "examples/*.json",
    "docs/examples/*.yaml",
    "docs/examples/*.yml",
    "docs/examples/*.json",
)


def load_document(path: Path) -> object:
    with path.open("r", encoding="utf-8") as stream:
        if path.suffix.lower() == ".json":
            return json.load(stream)
        return yaml.safe_load(stream)


def example_paths() -> list[Path]:
    return sorted({path for pattern in DEFAULT_PATTERNS for path in ROOT.glob(pattern)})


def validate_paths(paths: Iterable[Path]) -> list[str]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    failures: list[str] = []

    for path in paths:
        try:
            document = load_document(path)
        except (OSError, json.JSONDecodeError, yaml.YAMLError) as error:
            failures.append(f"{path}: could not parse: {error}")
            continue

        errors = sorted(validator.iter_errors(document), key=lambda error: list(error.path))
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            failures.append(f"{path}:{location}: {error.message}")

    return failures


def main(arguments: list[str] | None = None) -> int:
    arguments = sys.argv[1:] if arguments is None else arguments
    paths = [Path(argument) for argument in arguments] if arguments else example_paths()
    if not paths:
        print("No PDL documents found.", file=sys.stderr)
        return 2

    failures = validate_paths(paths)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print(f"Validated {len(paths)} PDL document(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
