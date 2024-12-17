import sys

def main():
    patterns = ["no-commit", "nocommit", "no-checkin", "nocheckin"]
    files = sys.argv[1:]
    for file in files:
        with open(file, 'r') as f:
            content = f.read().lower()
            for pattern in patterns:
                if pattern in content:
                    print(f"Pattern '%s' found in file: %s" % (pattern, file))
                    exit(1)
            
    exit(0)
