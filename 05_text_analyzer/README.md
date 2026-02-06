# Text Analyzer (Text File → CSV Reports)

A Python program that reads a text file, performs detailed analysis, and generates multiple CSV reports.  
This project is part of a Python learning portfolio and demonstrates practical text processing, file handling, and structured CSV output.

---

## What This Program Does

The Text Analyzer reads a `.txt` file and calculates:

- Number of non-empty lines
- Number of sentences (`.`, `!`, `?`)
- Total word count
- Character count (with and without spaces)
- Shortest and longest words
- Frequency of each word
- Top 10 most frequent words

All results are saved into well-structured CSV files.

---

## Project Structure

05_text_analyzer/
│
├── main.py
├── sample.txt
├── output/
│ ├── analysis_summary.csv
│ ├── frequency_word.csv
│ ├── sorted_frequency_word.csv
│ └── top_10_words.csv


### Why an `output/` Folder?
This project generates **multiple CSV files**.  
Using an `output/` folder keeps results organized and avoids clutter in the main directory.  
Other portfolio projects with minimal output do not use folders.

---

## How to Run

1. Make sure Python 3 is installed
2. Place your text file in the same directory (or use `sample.txt`)
3. Run the script:

```bash
python text_analyzer.py
```


