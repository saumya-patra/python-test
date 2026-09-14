import os

folder = os.path.dirname(os.path.abspath(__file__))
count = sum(1 for entry in os.scandir(folder) if entry.is_file())
print(f"number for files: {count}")
