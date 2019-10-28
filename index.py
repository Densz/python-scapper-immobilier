from src.Form import Form
from src.GoogleSheet import GoogleSheet
from pprint import pprint


class App:
    def __init__(self):
        self.form = Form()
        self.gSheet = GoogleSheet()

    def main(self):
        self.form.get_form()
        print(self.form.get_result())


App().main()
