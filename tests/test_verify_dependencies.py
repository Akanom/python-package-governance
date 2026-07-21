from pathlib import Path

from scripts.verify_dependencies import dependency_errors


def write_project(tmp_path: Path, dependency: str) -> None:
    (tmp_path / "pyproject.toml").write_text(
        "[build-system]\n"
        'requires = ["setuptools>=77,<82"]\n'
        'build-backend = "setuptools.build_meta"\n\n'
        '[project]\nname = "demo"\nversion = "1.0"\n'
        f'dependencies = ["{dependency}"]\n',
        encoding="utf-8",
    )


def test_accepts_bounded_requirement(tmp_path: Path) -> None:
    write_project(tmp_path, "numpy>=1.23,<3")
    assert dependency_errors(tmp_path) == []


def test_rejects_unbounded_requirement(tmp_path: Path) -> None:
    write_project(tmp_path, "numpy>=1.23")
    assert "upper bound" in dependency_errors(tmp_path)[0]


def test_rejects_direct_url(tmp_path: Path) -> None:
    write_project(tmp_path, "demo @ https://example.invalid/demo.whl")
    assert any("direct URL" in error for error in dependency_errors(tmp_path))


def test_rejects_unbounded_optional_dependency(tmp_path: Path) -> None:
    write_project(tmp_path, "numpy>=1.23,<3")
    with (tmp_path / "pyproject.toml").open("a", encoding="utf-8") as stream:
        stream.write('\n[project.optional-dependencies]\nplots = ["matplotlib>=3.8"]\n')
    assert any(
        "optional-dependencies.plots" in error for error in dependency_errors(tmp_path)
    )
