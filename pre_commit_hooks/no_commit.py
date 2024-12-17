import sys

patterns = ["no-commit", "nocommit", "no-checkin", "nocheckin"]


def check_file(filename):
    with open(filename, 'r') as f:
        content = f.read().lower()
        for pattern in patterns:
            if pattern in content:
                print(f"Pattern '{pattern}' found in file: {filename}")
                exit(1)


def main():
    files = sys.argv[1:]
    for filename in files:
        try:
            check_file(filename)
        except Exception:
            print(f"Error reading file contents for file: {filename}")
            exit(1)
    exit(0)
