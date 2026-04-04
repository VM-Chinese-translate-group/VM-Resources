import hashlib
from pathlib import Path

RESOURCE_DIR: Path = Path("resourcepack")


def calc_md5(file_path: Path) -> str:
    hasher = hashlib.md5()

    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def generate_md5_files() -> list[Path]:
    generated: list[Path] = []

    for zip_file in RESOURCE_DIR.rglob("*.zip"):
        md5_value: str = calc_md5(zip_file)

        md5_file: Path = zip_file.with_suffix(".md5")
        md5_file.write_text(md5_value + "\n", encoding="utf-8")

        generated.append(md5_file)
        print(f"Generated: {md5_file} -> {md5_value}")

    return generated


if __name__ == "__main__":
    generate_md5_files()
