# Email Validator (CSV-based)

A beginner-friendly Python project that reads emails from a CSV file,
validates them using a set of predefined rules, and separates valid and
invalid records into different CSV files.

---

## Features

- Checks that emails contain only safe characters: letters, digits, `. _ - @`
- Validates standard email formatting rules:
  - Exactly one `@` symbol
  - Valid local and domain parts
  - Domain and local parts do not start or end with `.`
  - No consecutive dots in local or domain
  - Top-level domain (TLD) at least 2 letters and alphabetic
- Provides clear error messages for invalid emails
- Demonstrates defensive CSV handling

---

## Project Structure

03_email_validator/
├── main.py             # Main Python script
├── README.md           # Project documentation
└── sample_input.csv    # Input CSV with example emails

---

## How It Works

1. Place your input CSV (`sample_input.csv`) in the same folder as `main.py`.  
2. Open terminal in this folder.  
3. Run the script:

```bash
python3 main.py
```

