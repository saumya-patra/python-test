from pathlib import Path
import sys


def analyze_text_file(file_path: str) -> dict:
    """Return a summary of the text file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    words = text.split()

    return {
        "file": str(path),
        "lines": len(lines),
        "words": len(words),
        "characters": len(text),
    }


def main() -> None:
    """Run the text analyzer from the command line."""
    if len(sys.argv) != 2:
        print("Usage: python text_agent.py <file.txt>")
        sys.exit(1)

    try:
        summary = analyze_text_file(sys.argv[1])
        print(f"File: {summary['file']}")
        print(f"Lines: {summary['lines']}")
        print(f"Words: {summary['words']}")
        print(f"Characters: {summary['characters']}")
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
