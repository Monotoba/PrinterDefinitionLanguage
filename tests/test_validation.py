from pathlib import Path

from scripts.validate_examples import example_paths, validate_paths


def test_all_examples_validate() -> None:
    paths = example_paths()

    assert paths
    assert validate_paths(paths) == []


def test_invalid_document_reports_required_fields(tmp_path: Path) -> None:
    invalid = tmp_path / "invalid.yaml"
    invalid.write_text("name: Incomplete printer\n", encoding="utf-8")

    failures = validate_paths([invalid])

    assert failures
    assert any("required property" in failure for failure in failures)
