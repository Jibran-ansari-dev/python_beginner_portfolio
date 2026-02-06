# Password Validator (CSV-based)

A beginner-friendly Python project that reads passwords from a CSV file,
validates them using a set of predefined rules, and separates valid and
invalid records into different CSV files.

---

## Features

- Checks minimum password length (at least 5 characters)
- Disallows spaces in passwords
- Restricts passwords to safe characters: letters, digits, and `!#$%^&*()-`
- Requires at least one uppercase letter
- Requires at least one digit
- Prevents three consecutive repeated characters
- Provides clear error messages for invalid passwords

---

## Project Structure

02_password_validator/
├── main.py             # Main Python script
├── README.md           # Project documentation
└── sample_input.csv    # Input CSV with example passwords

---

## How It Works

1. Place your input CSV (`sample_input.csv`) in the same folder as `main.py`.  
2. Open terminal in this folder.  
3. Run the script:

```bash
python3 main.py
```
4. After running:
- `valid_records.csv` → contains valid passwords
- `invalid_records.csv` → contains invalid passwords with error messages

