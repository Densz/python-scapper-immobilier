import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheet:
    __SCOPE = [
        "https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    __creds = ServiceAccountCredentials.from_json_keyfile_name(
        "./config/credentials.json", __SCOPE)
    __client = gspread.authorize(__creds)

    def __init__(self):
        self.__sheet = self.__client.open("Immobilier").sheet1

    def get_records(self):
        return self.__sheet.get_all_records()

    def get_row_count(self):
        return self.__sheet.row_count

    def insert_row(self, array):
        return self.__sheet.insert_row(array, 8)
