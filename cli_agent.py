import sys
from pathlib import Path


def count_keyword_in_file(file_path: str, keyword: str) -> int:
    """Count how many times a keyword appears in a text file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    text = path.read_text(encoding="utf-8")
    return text.lower().count(keyword.lower())


def main() -> None:
    """Simple CLI agent for basic text analysis."""
    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        keyword = sys.argv[2]
    elif len(sys.argv) == 1:
        file_path = input("Enter a file path: ").strip()
        keyword = input("Enter a keyword to search: ").strip()
    else:
        print("Usage: python cli_agent.py <file.txt> <keyword>")
        sys.exit(1)

    try:
        count = count_keyword_in_file(file_path, keyword)
        print(f"The keyword '{keyword}' appears {count} times in {file_path}.")
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
