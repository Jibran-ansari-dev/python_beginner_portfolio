"""
Combined Validator (CSV-based)

Validates usernames, passwords, and emails from a CSV file.
Writes valid records to one CSV and invalid records (with errors) to another.
"""

import csv

# -----------------------------
# Configuration: input/output
# -----------------------------
INPUT_FILE = "sample_input.csv"
VALID_OUTPUT = "valid_records.csv"
INVALID_OUTPUT = "nvalid_records.csv"


# -----------------------------
# Rule functions
# -----------------------------

def rule_not_empty(value, field):
    """Check that a field is not empty."""
    if not value:
        return False, "cannot be empty"
    return True, ""


# --- Username rules ---
def rule_username_min_length(value):
    """Username must be at least 5 characters."""
    if len(value) < 5:
        return False, "must be at least 5 characters"
    return True, ""


def rule_username_no_spaces(value):
    """Username must not contain spaces."""
    for char in value:
        if char.isspace():
            return False, "no spaces allowed"
    return True, ""


def rule_username_starts_with_letter(value):
    """Username must start with a letter."""
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
            return False, f"invalid character {char}"
    return True, ""


username_rules = [
    lambda v: rule_not_empty(v, "username"),
    rule_username_min_length,
    rule_username_no_spaces,
    rule_username_starts_with_letter,
    rule_username_only_safe_chars,
    rule_username_no_double_underscores
]


# --- Password rules ---
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
    """Password may only contain letters, digits, and safe symbols."""
    safe_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%^&*()-"
    for char in value:
        if char not in safe_chars:
            return False, f"invalid character | {char}"
    return True, ""


def rule_password_no_triple_repeats(value):
    """Password must not have three repeated characters consecutively."""
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            return False, "cannot have three repeated characters consecutively"
    return True, ""


def rule_password_has_uppercase(value):
    """Password must contain at least one uppercase letter."""
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


password_rules = [
    lambda v: rule_not_empty(v, "password"),
    rule_password_min_length,
    rule_password_no_space,
    rule_password_only_safe_chars,
    rule_password_has_digit,
    rule_password_has_uppercase,
    rule_password_no_triple_repeats
]


# --- Email rules ---
def valid_email_format(value):
    """Check standard email formatting rules."""
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
        return False, "domain cannot start or end with '.'"
    if local.startswith(".") or local.endswith("."):
        return False, "local cannot start or end with '.'"
    if '..' in domain:
        return False, "domain has consecutive dots"
    if ".." in local:
        return False, "local has consecutive dots"

    tld = domain.split(".")[-1]
    if len(tld) < 2:
        return False, "TLD too short"
    if not tld.isalpha():
        return False, "TLD can only contain letters"

    return True, ""


def rule_email_only_safe_chars(value):
    """Email may only contain letters, digits, and safe symbols."""
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-@"
    for char in value:
        if char not in allowed:
            return False, f"contains invalid character {char}"
    return True, ""


email_rules = [
    lambda v: rule_not_empty(v, "email"),
    rule_email_only_safe_chars,
    valid_email_format
]


# -----------------------------
# Validation engine
# -----------------------------
def is_field_ok(field, rules):
    """Apply rules to a field; return True and None if all pass."""
    for rule in rules:
        passed, message = rule(field)
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

        valid_fieldnames = ["username", "password", "email"]
        invalid_fieldnames = ["username", "password", "email", "error"]
        required_fields = ["username", "password", "email"]

        reader = csv.DictReader(file)
        valid_writer = csv.DictWriter(valid_file, fieldnames=valid_fieldnames)
        invalid_writer = csv.DictWriter(invalid_file, fieldnames=invalid_fieldnames)

        # Check if all required columns exist
        missing_headers = [field for field in required_fields if field not in reader.fieldnames]
        if missing_headers:
            raise ValueError(f"CSV is missing required columns: {missing_headers}")

        # Write CSV headers
        valid_writer.writeheader()
        invalid_writer.writeheader()

        # Process each row
        for row in reader:
            is_username_valid, username_error = is_field_ok(row["username"], username_rules)
            is_password_valid, password_error = is_field_ok(row["password"], password_rules)
            is_email_valid, email_error = is_field_ok(row["email"], email_rules)

            if is_username_valid and is_password_valid and is_email_valid:
                valid_writer.writerow(row)
            else:
                errors = []
                if username_error:
                    errors.append(f"username: {username_error}")
                if password_error:
                    errors.append(f"password: {password_error}")
                if email_error:
                    errors.append(f"email: {email_error}")

                row["error"] = " | ".join(errors)
                invalid_writer.writerow(row)

except FileNotFoundError as e:
    print("File not found:", e)
except PermissionError as e:
    print("Permission denied:", e)
except Exception as e:
    print("Unexpected error:", e)
else:
    print("Validation completed successfully.")
finally:
    print("Validation attempt finished.")
