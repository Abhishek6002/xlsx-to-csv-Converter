import sys
import os
import pandas as pd
import requests

if len(sys.argv) < 2:
    print("Please provide an input file")
    sys.exit()


input_file = sys.argv[1]

if input_file.startswith("https://docs.google.com/spreadsheets/"):

    print("Google Sheets link detected")

    url_parts = input_file.split("/")
    spreadsheet_id = url_parts[5]

    download_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=xlsx"

    response = requests.get(download_url)

    print("Status code:", response.status_code)

    if response.status_code == 200:
        downloaded_file = spreadsheet_id + ".xlsx"

        with open(downloaded_file, "wb") as file:
            file.write(response.content)

        print("Excel file downloaded successfully!")
        input_file = downloaded_file
    else:
        print("Download failed!")
        sys.exit()
else:
    print("Local Excel file detected")


if not os.path.exists(input_file):
    print("File does not exist!")
    sys.exit()



excel_file = pd.ExcelFile(input_file)
print("Sheet Names:", excel_file.sheet_names)

output_dir = os.path.splitext(input_file)[0]
os.makedirs(output_dir, exist_ok=True)


for sheet in excel_file.sheet_names:

    df = pd.read_excel(input_file, sheet_name=sheet)

    csv_path = os.path.join(output_dir, sheet + ".csv")

    df.to_csv(csv_path, index=False)

    print("Converted:", sheet)

print("Conversion completed!")
