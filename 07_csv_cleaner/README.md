# CSV Cleaner (Username, Password, Email)

A Python program that reads a CSV file containing usernames, passwords, and emails,  
cleans the values by removing spaces (and lowercasing usernames and emails),  
and generates a cleaned CSV output.  

This project is part of a Python learning portfolio and demonstrates practical file handling, data cleaning, exception handling, and structured CSV output.

---

## What This Program Does

- Reads a CSV file (`input.csv`) with columns: `username`, `password`, `email`  
- Removes all whitespace from each value  
- Converts `username` and `email` to lowercase  
- Writes the cleaned data to a new CSV file in the `output/` folder  

The program handles:  
- Missing columns  
- Missing files  
- Permission errors  
- Unexpected row errors  

---

## Project Structure

05_csv_cleaner/
│
├── main.py
├── input.csv
├── output/
│ └── validoutput.csv


### Why an `output/` Folder?
The cleaned CSV file is placed in a dedicated `output/` folder to keep the project directory organized, especially when multiple output files are produced across different portfolio programs.

---

## How to Run

1. Make sure Python 3 is installed  
2. Place your CSV file in the same directory (or use `input.csv`)  
3. Run the script:

```bash
python csv_cleaner.py
```
