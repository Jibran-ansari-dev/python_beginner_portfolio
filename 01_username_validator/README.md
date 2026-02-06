# Username Validator (CSV-based)

A beginner-friendly Python project that reads usernames from a CSV file,
validates them using a set of predefined rules, and separates valid and
invalid records into different CSV files.

---

## Features

- Checks minimum username length (at least 5 characters)
- Disallows usernames made of digits only
- Prevents spaces and double underscores
- Restricts usernames to safe characters (letters, digits, dots, hyphens)
- Requires usernames to start with a letter
- Demonstrates defensive CSV handling (including intentional errors)
- Provides clear error messages for invalid usernames

---

## Project Structure

01_username_validator/
├── main.py               # Main Python script
├── README.md             # Project documentation
├── sample_input.csv      # Input CSV with example usernames

---

## How It Works

1. Place your input CSV (`sample_input.csv`) in the same folder as `main.py`.
2. Open terminal in this folder.
3. Run the script:

```bash
python3 main.py
```
