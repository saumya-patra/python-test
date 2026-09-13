import csv
import sys
from pathlib import Path


def filter_approved_rows(input_path: str, output_path: str) -> int:
    """Read a CSV file and keep only rows with status == 'Approved'."""
    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    approved_rows = []
    with input_file.open("r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

        for row in rows:
            if row.get("status", "").strip().lower() == "approved":
                approved_rows.append(row)

    with output_file.open("w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["name", "status", "amount"])
        writer.writeheader()
        writer.writerows(approved_rows)

    return len(approved_rows)


def main() -> None:
    """Run the script from the command line."""
    if len(sys.argv) not in (2, 3):
        print("Usage: python sample_agent.py <input_csv> [output_csv]")
        print("Example: python sample_agent.py sample_input.csv filtered_output.csv")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) == 3 else "filtered_output.csv"

    try:
        count = filter_approved_rows(input_path, output_path)
        print(f"Saved {count} approved rows to {output_path}")
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
