import io
import tarfile
import zipfile
from pathlib import Path

from scripts.inspect_dist import inspect


def test_clean_wheel_passes(tmp_path: Path) -> None:
    wheel = tmp_path / "demo-1-py3-none-any.whl"
    with zipfile.ZipFile(wheel, "w") as archive:
        archive.writestr("demo/__init__.py", "")
    assert inspect(wheel, set(), 250_000_000, 20_000)["errors"] == []


def test_secret_in_sdist_fails(tmp_path: Path) -> None:
    sdist = tmp_path / "demo-1.tar.gz"
    with tarfile.open(sdist, "w:gz") as archive:
        payload = b"SECRET"
        item = tarfile.TarInfo("demo-1/.env")
        item.size = len(payload)
        archive.addfile(item, io.BytesIO(payload))
    report = inspect(sdist, set(), 250_000_000, 20_000)
    assert any("sensitive" in error for error in report["errors"])


def test_path_traversal_fails(tmp_path: Path) -> None:
    wheel = tmp_path / "demo-1-py3-none-any.whl"
    with zipfile.ZipFile(wheel, "w") as archive:
        archive.writestr("../escape.py", "")
    report = inspect(wheel, set(), 250_000_000, 20_000)
    assert any("unsafe" in error for error in report["errors"])


def test_private_key_content_fails(tmp_path: Path) -> None:
    wheel = tmp_path / "demo-1-py3-none-any.whl"
    with zipfile.ZipFile(wheel, "w") as archive:
        marker = "-----BEGIN " + "PRIVATE KEY-----\n"
        archive.writestr("demo/key.txt", marker)
    report = inspect(wheel, set(), 250_000_000, 20_000)
    assert any("private key" in error for error in report["errors"])


def test_backup_snapshot_name_fails(tmp_path: Path) -> None:
    wheel = tmp_path / "demo-1-py3-none-any.whl"
    with zipfile.ZipFile(wheel, "w") as archive:
        archive.writestr("demo/model.before_patch.py", "")
    report = inspect(wheel, set(), 250_000_000, 20_000)
    assert any("sensitive file name" in error for error in report["errors"])
