"""
Password Validator (CSV-based)

Reads passwords from a CSV file and validates them
according to a set of predefined rules.

Valid records are written to a separate CSV file.
Invalid records are written to another CSV file along with
the validation error message.

Designed as a beginner-friendly portfolio project.
"""

import csv

# -----------------------------
# Configuration: input/output
# -----------------------------

INPUT_FILE = "sample_input.csv"
OUTPUT_VALID = "valid_records.csv"
OUTPUT_INVALID = "invalid_records.csv"

# -----------------------------
# Password validation rules
# -----------------------------

def rule_password_min_length(value):
    """Password must be at least 5 characters."""
    if len(value) < 5:
        return False, "must be at least 5 characters"
    return True, ""

def rule_password_no_space(value):
    """Password must not contain spaces."""
    if " " in value:
        return False, "no spaces allowed"
    return True, ""

def rule_password_only_safe_chars(value):
    """Password may only contain letters, digits, and special characters !#$%^&*()-"""
    safe_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%^&*()-"
    for char in value:
        if char not in safe_chars:
            return False, f"invalid character '{char}'"
    return True, ""

def rule_password_no_triple_repeats(value):
    """Password cannot have three consecutive repeated characters."""
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            return False, "cannot have three repeated characters consecutively"
    return True, ""

def rule_password_has_uppercase(value):
    """Password must contain at least one uppercase character."""
    for ch in value:
        if ch.isupper():
            return True, ""
    return False, "must have an uppercase character"

def rule_password_has_digit(value):
    """Password must contain at least one digit."""
    for ch in value:
        if ch.isdigit():
            return True, ""
    return False, "must have at least one digit"

# List of rules applied in order
password_rules = [
    rule_password_min_length,
    rule_password_no_space,
    rule_password_only_safe_chars,
    rule_password_has_digit,
    rule_password_has_uppercase,
    rule_password_no_triple_repeats
]

# -----------------------------
# Validation engine
# -----------------------------

def is_password_ok(password, rules):
    """
    Apply validation rules to a password.

    Returns:
        (bool, str): Validation result and error message (if any)
    """
    for rule in rules:
        passed, message = rule(password)
        if not passed:
            return False, message
    return True, ""

# -----------------------------
# CSV processing
# -----------------------------

try:
    with open(INPUT_FILE, "r", newline="") as file, \
         open(OUTPUT_VALID, "w", newline="") as valid_file, \
         open(OUTPUT_INVALID, "w", newline="") as invalid_file:

        reader = csv.DictReader(file)

        # Writers for valid and invalid records
        valid_writer = csv.DictWriter(valid_file, fieldnames=["username","password","email"])
        invalid_writer = csv.DictWriter(invalid_file, fieldnames=["username","password","email","error"])

        valid_writer.writeheader()
        invalid_writer.writeheader()

        for row in reader:
            try:
                password = row["password"]
            except KeyError:
                print("Row missing 'password' key. Skipping row.")
                continue

            is_valid, error = is_password_ok(password, password_rules)

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
    print("Password validation completed successfully.")
finally:
    print("Validation attempt finished.")
