import argparse
from pathlib import Path


def read_text(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def count_words(text: str) -> int:
    return len(text.split())


def search_keyword(text: str, keyword: str) -> int:
    return text.lower().count(keyword.lower())


def summary(text: str) -> str:
    lines = text.splitlines()
    words = count_words(text)
    chars = len(text)
    return (
        f"Lines: {len(lines)}\n"
        f"Words: {words}\n"
        f"Characters: {chars}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple multi-command local assistant")
    parser.add_argument("--file", required=True, help="Text file to analyze")
    parser.add_argument("--command", choices=["help", "count", "search", "summary"], default="help")
    parser.add_argument("--keyword", default="AI", help="Keyword to search for")
    args = parser.parse_args()

    try:
        text = read_text(args.file)

        if args.command == "help":
            print("Available commands: help, count, search, summary")
        elif args.command == "count":
            print(f"Word count: {count_words(text)}")
        elif args.command == "search":
            print(f"Keyword '{args.keyword}' found {search_keyword(text, args.keyword)} times.")
        elif args.command == "summary":
            print(summary(text))
    except Exception as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
