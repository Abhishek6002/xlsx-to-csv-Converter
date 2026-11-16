# XLSX to CSV Converter

A Python-based tool that converts Excel workbooks (`.xlsx`) and Google Sheets into CSV files. It automatically detects the input type, processes every worksheet, and generates a separate CSV file for each sheet.

## Features

- **Local Excel Support:** Accepts `.xlsx` files as command-line arguments.
- **Google Sheets Support:** Accepts Google Sheets URLs and downloads the spreadsheet in Excel format.
- **Automatic Sheet Detection:** Identifies all worksheets in the workbook.
- **Multiple Sheet Conversion:** Converts every worksheet into an individual CSV file.
- **Automatic Output Directory:** Creates a separate directory based on the input filename.
- **Clean CSV Output:** Excludes unnecessary row indexes from generated CSV files.

## Technologies Used

- Python 3.11
- Pandas
- OpenPyXL
- Requests

## Project Structure

```text
xlsx-to-csv-converter/
│
├── converter.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/Abhishek6002/xlsx-to-csv-converter.git
```

**2. Navigate to the project directory**

```bash
cd xlsx-to-csv-converter
```

**3. Install the required dependencies**

```bash
py -3.11 -m pip install -r requirements.txt
```

## Usage

### 1. Convert a Local Excel File

Run the converter with the Excel file path:

```bash
py -3.11 converter.py "sample_data.xlsx"
```

### 2. Convert a Google Sheet

Run the converter with a Google Sheets URL:

```bash
py -3.11 converter.py "YOUR_GOOGLE_SHEETS_URL"
```

**Note:** The Google Sheet must be accessible to the downloader. For the current implementation, use a sheet shared with anyone who has the link.

## How It Works

1. Accepts the input through command-line arguments.
2. Detects whether the input is a local Excel file or a Google Sheets URL.
3. If the input is a Google Sheets URL, extracts the spreadsheet ID and downloads the spreadsheet as an `.xlsx` file.
4. Opens the Excel workbook using Pandas.
5. Identifies all available worksheets.
6. Creates an output directory.
7. Reads each worksheet and converts it into a separate CSV file.
8. Saves the generated CSV files without row indexes.

## Example Output

For an Excel workbook containing two worksheets:

```text
sample_data/
│
├── Office Supply Sales.csv
└── Food Sales.csv
```

Each worksheet is converted into its own CSV file.

## Future Improvements

The following improvements are planned:

- **Error Handling:** Handle invalid file formats, missing files, inaccessible Google Sheets, and network failures.
- **Code Refactoring:** Organize the converter into reusable functions for better maintainability.
- **Unit Testing:** Implement automated tests using Python's `unittest` framework.
- **Input Validation:** Improve validation of command-line arguments and Google Sheets URLs.
- **Documentation:** Add more examples and usage instructions as the project develops.

## Current Status

The basic conversion functionality is implemented and tested for both local Excel files and accessible Google Sheets.

Further improvements, including error handling, code refactoring, and automated unit testing, are planned.
