"""
Email Validator (CSV-based)

Reads emails from a CSV file and validates them
according to predefined rules.

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
VALID_OUTPUT = "valid_records.csv"
INVALID_OUTPUT = "invalid_records.csv"

# -----------------------------
# Email validation rules
# -----------------------------

def rule_email_only_safe_chars(value):
    """Email may only contain letters, digits, and . _ - @"""
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-@"
    for char in value:
        if char not in allowed:
            return False, f"contains invalid character '{char}'"
    return True, ""

def valid_email_format(value):
    """Check email format: one @, valid local and domain parts, valid TLD"""
    if value.count('@') != 1:
        return False, "must contain exactly one '@'"
    if " " in value:
        return False, "email cannot contain spaces"

    local, _, domain = value.partition('@')
    if not local:
        return False, "no characters before '@'"
    if "." not in domain:
        return False, "no '.' in domain part"
    if domain.startswith('.') or domain.endswith('.'):
        return False, "domain starts or ends with '.'"
    if local.startswith('.') or local.endswith('.'):
        return False, "local part starts or ends with '.'"
    if '..' in domain:
        return False, "domain has consecutive dots"
    if '..' in local:
        return False, "local part has consecutive dots"
    tld = domain.split(".")[-1]
    if len(tld) < 2:
        return False, "TLD too short"
    if not tld.isalpha():
        return False, "TLD can only contain alphabets"

    return True, ""

# List of rules applied in order
email_rules = [rule_email_only_safe_chars, valid_email_format]

# -----------------------------
# Validation engine
# -----------------------------

def is_email_ok(email, rules):
    """
    Apply validation rules to an email.

    Returns:
        (bool, str | None): Validation result and error message (if any)
    """
    for rule in rules:
        passed, message = rule(email)
        if not passed:
            return False, message
    return True, None

# -----------------------------
# CSV processing
# -----------------------------

try:
    with open(INPUT_FILE, "r", newline="") as file, \
         open(VALID_OUTPUT, "w", newline="") as valid_file, \
         open(INVALID_OUTPUT, "w", newline="") as invalid_file:

        reader = csv.DictReader(file)
        valid_fieldnames = ["username","password","email"]
        invalid_fieldnames = ["username","password","email","error"]

        valid_writer = csv.DictWriter(valid_file, fieldnames=valid_fieldnames)
        invalid_writer = csv.DictWriter(invalid_file, fieldnames=invalid_fieldnames)

        # Write headers
        valid_writer.writeheader()
        invalid_writer.writeheader()

        # Process each row
        for row in reader:
            try:
                email = row["email"]
            except KeyError:
                print("Row missing 'email' key. Skipping row.")
                continue

            is_valid, error = is_email_ok(email, email_rules)

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
    print("Email validation completed successfully.")
finally:
    print("Validation attempt finished.")
