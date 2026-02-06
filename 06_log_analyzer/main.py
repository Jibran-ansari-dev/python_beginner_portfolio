"""
Log Analyzer Program

Reads a log file containing timestamped actions and statuses,
then produces chronological output and summary statistics.

Designed as a portfolio project demonstrating:
- File parsing
- Datetime handling
- Dictionary-based aggregation
- CSV report generation
"""

import csv
from datetime import datetime
import os


def get_file_path():
    """
    Prompts the user for a log file path.

    If the user presses Enter, a default sample file path is used.

    Returns:
        str: Path to the log file.
    """
    INPUT_FILE = "sample_log.txt"
    return input("Enter the file path or press Enter to use default: ") or INPUT_FILE


def read_text_file(path):
    """
    Reads the contents of a text file.

    Args:
        path (str): Path to the file.

    Returns:
        str | None: File content if successful, otherwise None.
    """
    try:
        with open(path, "r", newline="") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {path} not found")
        return None


def log_analyzer():
    """
    Main controller function for log analysis workflow.
    """
    path = get_file_path()
    log = read_text_file(path)

    if log is None:
        return

    action_count = {}
    status_count = {}
    first_ts = {}
    last_ts = {}
    all_entries = []

    lines = log.splitlines()

    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue

        parts = line.split(",")

        # Skip malformed log entries
        if len(parts) != 3:
            continue

        timestamp_str = parts[0].strip()
        action = parts[1].strip()
        status = parts[2].strip()

        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

        all_entries.append((timestamp, action, status))

        # Count actions and statuses
        action_count[action] = action_count.get(action, 0) + 1
        status_count[status] = status_count.get(status, 0) + 1

        # Track first and last occurrence timestamps per action
        if action not in first_ts or timestamp < first_ts[action]:
            first_ts[action] = timestamp

        if action not in last_ts or timestamp > last_ts[action]:
            last_ts[action] = timestamp

    # Sort log entries chronologically
    all_entries.sort(key=lambda x: x[0])

    print("\nChronological Log")
    print("-----------------")
    for ts, action, status in all_entries:
        print(f"{ts} | {action} | {status}")

    print("\nAction Summary")
    print("-----------------")
    for action, count in action_count.items():
        print(
            f"{action}: {count} times "
            f"(first: {first_ts[action]}, last: {last_ts[action]})"
        )

    print("\nStatus Summary")
    print("-----------------")
    for status, count in status_count.items():
        print(f"{status}: {count}")

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    # Write chronological log CSV
    chronological_log = "output/chronological_log.csv"

    with open(chronological_log, "w", newline="") as file:
        fieldnames = ["timestamp", "action", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for timestamp, action, status in all_entries:
            writer.writerow({
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "action": action,
                "status": status
            })


if __name__ == "__main__":
    log_analyzer()
