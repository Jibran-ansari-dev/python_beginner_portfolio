# Combined Validator (CSV-based)

A beginner-friendly Python project that validates usernames, passwords,
and emails from a CSV file. Valid records are written to one CSV, while
invalid records (with errors) are written to another CSV.

---

## Features

- **Username validation**:
  - Minimum 5 characters
  - No spaces
  - Must start with a letter
  - No double underscores (`__`)
  - Only letters, digits, dots, and hyphens allowed

- **Password validation**:
  - Minimum 5 characters
  - No spaces
  - Only letters, digits, and safe symbols (`!#$%^&*()-`)
  - At least one uppercase letter
  - At least one digit
  - No three consecutive repeated characters

- **Email validation**:
  - Only letters, digits, and `. _ - @`
  - Valid standard format (`local@domain.tld`)
  - No consecutive dots, domain/local parts do not start/end with `.`
  - TLD must be at least 2 letters

- Provides clear error messages for invalid records
- Demonstrates CSV handling and defensive programming

---

## Project Structure

04_combined_validator/
├── main.py             # Main Python script
├── README.md           # Project documentation
└── sample_input.csv    # Input CSV with usernames, passwords, and emails

---

## How It Works

1. Place your input CSV (`sample_input.csv`) in the same folder as `main.py`.  
2. Open terminal in this folder.  
3. Run the script:

```bash
python3 main.py
```
