# Contributing to PDL

Contributions are welcome, especially real printer definitions, schema fixes,
and reports from slicer or firmware integrations.

## Before opening a pull request

1. Create a branch from `main`.
2. Keep schema changes backward compatible unless a major-version change is intended.
3. Add or update an example demonstrating the proposed behavior.
4. Run `python -m pytest` and `python scripts/validate_examples.py`.
5. Update the specification and changelog when behavior changes.

## Design guidelines

- Use explicit units in field names or specification text.
- Prefer broadly applicable concepts over slicer-specific settings.
- Keep identifiers stable, lowercase, and machine-readable.
- Document whether a field is required, optional, or implementation-defined.
- Do not include proprietary profiles unless you have permission to redistribute them.

Please use GitHub Issues for proposals that change the schema or its semantics so
implementers can discuss compatibility before code is submitted.
