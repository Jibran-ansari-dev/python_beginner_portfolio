"""
CSV Cleaner Program

Reads a CSV file containing usernames, passwords, and emails,
cleans the values by removing spaces (and lowercasing where appropriate),
and writes the cleaned data to a new CSV file.

Designed as a portfolio project demonstrating:
- File handling with CSVs
- Data cleaning
- Exception handling
- Output organization
"""

import csv
import os

# Default input and output files
INPUT_FILE = "input.csv"
OUTPUT_FILE = "output/validoutput.csv"


def no_space(value: str) -> str:
    """
    Removes all whitespace from a string.

    Args:
        value (str): The string to clean.

    Returns:
        str: String without any spaces.
    """
    cleaned = ""
    for ch in value:
        if not ch.isspace():
            cleaned += ch
    return cleaned


def no_space_lower(value: str) -> str:
    """
    Removes all whitespace from a string and converts it to lowercase.

    Args:
        value (str): The string to clean.

    Returns:
        str: Lowercased string without spaces.
    """
    cleaned = ""
    for ch in value:
        if not ch.isspace():
            cleaned += ch
    return cleaned.lower()


def clean_csv():
    """
    Main function to clean the CSV file.

    Reads INPUT_FILE, removes spaces from all values, lowercases
    usernames and emails, and writes the cleaned data to OUTPUT_FILE.

    Handles:
    - Missing file
    - Permission errors
    - Missing columns
    - Unexpected row errors

    Creates the output folder if it doesn't exist.
    """
    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    fieldnames = ["username", "password", "email"]

    try:
        with open(INPUT_FILE, 'r', newline="") as infile, \
             open(OUTPUT_FILE, 'w', newline="") as outfile:

            reader = csv.DictReader(infile)

            # Check required columns
            required_fields = {"username", "password", "email"}
            missing = required_fields - set(reader.fieldnames or [])
            if missing:
                print(f"CSV missing required columns: {missing}")
                return

            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                try:
                    username = row.get("username") or ""
                    password = row.get("password") or ""
                    email = row.get("email") or ""

                    clean_username = no_space_lower(username)
                    clean_password = no_space(password)
                    clean_email = no_space_lower(email)

                    writer.writerow({
                        "username": clean_username,
                        "password": clean_password,
                        "email": clean_email
                    })

                except KeyError as e:
                    print(f"Row missing key {e}, skipping")
                except Exception as e:
                    print("Unexpected error in row:", e)

    except FileNotFoundError as e:
        print("File not found:", e)
    except PermissionError as e:
        print("Permission denied:", e)
    except Exception as e:
        print("Unexpected error:", e)
    else:
        print("CSV file cleaned successfully")
    finally:
        print("CSV file cleaning attempt finished")


if __name__ == "__main__":
    clean_csv()
