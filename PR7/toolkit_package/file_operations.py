"""Safe text-file operations for the Multi-Utility Toolkit."""

from pathlib import Path


def _safe_path(filename: str) -> Path:
    """Keep user-created files inside the project's data directory."""
    name = filename.strip()
    if not name:
        raise ValueError("Filename cannot be empty.")
    if Path(name).name != name or name in {".", ".."}:
        raise ValueError("Use a filename only; directory paths are not allowed.")
    if not name.lower().endswith(".txt"):
        name += ".txt"
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir / name


def create_file(filename: str, content: str = "") -> Path:
    path = _safe_path(filename)
    path.write_text(content, encoding="utf-8")
    return path


def write_file(filename: str, content: str) -> Path:
    path = _safe_path(filename)
    path.write_text(content, encoding="utf-8")
    return path


def append_file(filename: str, content: str) -> Path:
    path = _safe_path(filename)
    with path.open("a", encoding="utf-8") as file:
        file.write(content)
    return path


def read_file(filename: str) -> str:
    path = _safe_path(filename)
    if not path.exists():
        raise FileNotFoundError(f"{path.name} does not exist.")
    return path.read_text(encoding="utf-8")


def list_files() -> list[str]:
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(exist_ok=True)
    return sorted(path.name for path in data_dir.glob("*.txt") if path.is_file())
