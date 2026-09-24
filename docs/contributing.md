# Contributing

Contributions of printer examples, schema corrections, implementation reports,
and documentation improvements are welcome.

Before submitting a pull request, run:

```bash
python scripts/validate_examples.py
python -m pytest -q
mkdocs build --strict
```

Schema changes should include a representative example and corresponding
specification update. See the repository's complete
[contribution guide](https://github.com/Monotoba/PrinterDefinitionLanguage/blob/main/CONTRIBUTING.md).
