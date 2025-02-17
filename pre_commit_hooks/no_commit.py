import sys

patterns = ["no-commit", "nocommit", "no-checkin", "nocheckin"]


def check_file(filename: str) -> (bool, str):
    """
    checks a file path for the existence of a no commit mark.

    Args:
        filename (str): the name of the file to test.

    Returns:
        bool: does the file contain the pattern
        str: optionally the pattern that was detected
    """
    with open(filename, 'r') as f:
        content = f.read().lower()
        for pattern in patterns:
            if pattern in content:
                return True, pattern
    return False, None


def main() -> int:
    """
    The main function of the check.
    It takes a list of files from the command line and checks each of them
    for the existence of the no-commit pattern.

    Args:
    Returns:
        int: the number of files that contain a no-commit pattern.
    """
    files = sys.argv[1:]
    findings = []
    for filename in files:
        try:
            has_finding, pattern = check_file(filename)
            if has_finding:
                findings.append((filename, pattern))
        except Exception:
            print(f"Error reading file contents for file: {filename}")
            exit(1)

    for finding in findings:
        print(f"Pattern '{finding[1]}' found in file: {finding[0]}")
    exit(len(findings))
