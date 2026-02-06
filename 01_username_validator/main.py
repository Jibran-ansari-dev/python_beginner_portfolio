"""
Username Validator (CSV-based)

This script reads usernames from a CSV file and validates them
according to a set of predefined rules.

Valid records are written to a separate CSV file.
Invalid records are written to another CSV file along with
the validation error message.

Designed as a portfolio-ready beginner Python project.
"""

import csv

# -----------------------------
# Configuration: input/output
# -----------------------------

INPUT_FILE = r"c:\Users\user\Desktop\PythonPortfolio\01_username_validator\input\sample.csv"
OUTPUT_VALID = r"c:\Users\user\Desktop\PythonPortfolio\01_username_validator\output\valid_records.csv"
OUTPUT_INVALID = r"c:\Users\user\Desktop\PythonPortfolio\01_username_validator\output\invalid_records.csv"


# -----------------------------
# Username validation rules
# -----------------------------

def rule_username_min_length(value):
    """Username must be at least 5 characters long."""
    if len(value) < 5:
        return False, "must be at least 5 characters"
    return True, ""


def rule_username_not_digits_only(value):
    """Username must not consist of digits only."""
    if value.isdigit():
        return False, "cannot be digits only"
    return True, ""


def rule_username_no_spaces(value):
    """Username must not contain whitespace characters."""
    for char in value:
        if char.isspace():
            return False, "no spaces allowed"
    return True, ""


def rule_username_starts_with_letter(value):
    """Username must start with an alphabetic character."""
    if not value[0].isalpha():
        return False, "must start with a letter"
    return True, ""


def rule_username_no_double_underscores(value):
    """Username must not contain double underscores."""
    if "__" in value:
        return False, "double underscore not allowed"
    return True, ""


def rule_username_only_safe_chars(value):
    """Username may only contain letters, digits, dots, and hyphens."""
    safe_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.-"
    for char in value:
        if char not in safe_chars:
            return False, f"invalid character '{char}'"
    return True, ""


# List of rules applied in order
username_rules = [
    rule_username_min_length,
    rule_username_not_digits_only,
    rule_username_no_double_underscores,
    rule_username_no_spaces,
    rule_username_only_safe_chars,
    rule_username_starts_with_letter,
]


# -----------------------------
# Validation engine
# -----------------------------

def is_username_valid(username, rules):
    """
    Apply validation rules to a username.

    Returns:
        (bool, str | None): Validation result and error message (if any)
    """
    for rule in rules:
        passed, message = rule(username)
        if not passed:
            return False, message
    return True, None


# -----------------------------
# CSV processing
# -----------------------------

try:
    with open(INPUT_FILE, "r", newline="") as infile, \
         open(OUTPUT_VALID, "w", newline="") as valid_file, \
         open(OUTPUT_INVALID, "w", newline="") as invalid_file:

        reader = csv.DictReader(infile)

        # Writers for valid and invalid records
        valid_writer = csv.DictWriter(
            valid_file,
            fieldnames=["username", "password", "email"],
            extrasaction="ignore"
        )

        invalid_writer = csv.DictWriter(
            invalid_file,
            fieldnames=["username", "password", "email", "error"],
            extrasaction="ignore"
        )

        valid_writer.writeheader()
        invalid_writer.writeheader()

        for row in reader:
            try:
                username = row["username1"]  # intentionally incorrect key for testing
            except KeyError:
                print("Row missing 'username' key. Skipping row.")
                continue

            is_valid, error = is_username_valid(username, username_rules)

            if is_valid:
                valid_writer.writerow(row)
            else:
                row["error"] = error
                invalid_writer.writerow(row)

except FileNotFoundError as e:
    print("File not found:", e)
except PermissionError as e:
    print("Permission denied:", e)
except Exception as e:
    print("Unexpected error:", e)
else:
    print("Username validation completed successfully.")
finally:
    print("Validation attempt finished.")
