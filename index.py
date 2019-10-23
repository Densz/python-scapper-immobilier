import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "./config/credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Immobilier").sheet1

data = sheet.get_all_records()
pprint(data)

numRows = sheet.row_count

insertRow = ["hello", 5, "red", "blue"]
sheet.insert_row(insertRow, 8)