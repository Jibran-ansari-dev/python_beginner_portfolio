# Log Analyzer (Log File → CSV Report)

A Python program that reads a timestamped log file, analyzes actions and statuses,  
and generates a chronological CSV report.  
This project is part of a Python learning portfolio and demonstrates practical file parsing, datetime handling, dictionary-based aggregation, and structured CSV output.

---

## What This Program Does

The Log Analyzer reads a `.txt` log file where each line has the format:


It calculates:

- Chronological list of all log entries
- Counts of each action
- Counts of each status
- First and last occurrence of each action

All results are saved into a CSV file in the `output/` folder.

---

## Project Structure

06_log_analyzer/
│
├── main.py
├── sample_log.txt
├── output/
│ └── chronological_log.csv


### Why an `output/` Folder?
The project produces **multiple CSV outputs** (chronological logs, summaries).  
Using an `output/` folder keeps the main directory clean and results organized.  
Other beginner projects with minimal output may not use folders.

---

## How to Run

1. Make sure Python 3 is installed
2. Place your log file in the same directory (or use `sample_log.txt`)
3. Run the script:

```bash
python log_analyzer.py
```

#SAmple output

Chronological Log
-----------------
2026-02-06 09:00:01 | Login | Success
2026-02-06 09:05:12 | Upload | Failed
...

Action Summary
-----------------
Login: 5 times (first: 2026-02-06 09:00:01, last: 2026-02-06 18:45:20)
Upload: 3 times (first: 2026-02-06 09:05:12, last: 2026-02-06 15:10:45)

Status Summary
-----------------
Success: 7
Failed: 3


