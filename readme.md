# Clean Messy CSV

A small Python utility that reads a messy CSV file, cleans common data issues, and writes a corrected version.

This project is designed as a simple, practical example of real-world data cleaning and scripting.

## Features

- Validates and standardises:
  - Email addresses
  - Mobile numbers
  - Dates
- Focuses on data integrity: the script does not invent missing    values. Invalid or junk data is removed, and missing fields remain empty.
- Outputs cleaned columns alongside the original data for easy comparison and verification
- Logs before and after info to the terminal
- Simple, readable, and easy to modify

## Project Structure
```
clean_messy_csv/
│
├── clean_messy_csv.py     # Main script
├── helpers.py             # Validation and cleaning functions
├── logging_setup.py       # Logging configuration
├── messy_data.csv         # Example input file
├── cleaned_data.csv       # Example output file
├── requirements.txt
└── README.md
```
## Requirements

- Python 3.10 or newer

Install dependencies:

```

pip install -r requirements.txt

```

## How to Run

1. Place your CSV file in the project folder.
2. Edit the input/output file names in `clean_messy_csv.py` if needed.
3. Run:

```

python clean_messy_csv.py

```

4. The cleaned file will be created.

## Example Use Case

This script is useful when:

- CSV data comes from multiple sources
- Email or phone formats are inconsistent
- Dates are in mixed formats
- You need a quick, reliable cleanup before importing into a system

## Author

Juliana Albertyn  
Delphi & SQL developer expanding into Python.
