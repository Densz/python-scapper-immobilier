from src.Form import Form
from src.GoogleSheet import GoogleSheet
from src.Scrapper import Scrapper
from pprint import pprint


class App:
    def __init__(self):
        self.formInput = {}
        self.gSheet = GoogleSheet()

    def main(self):
        form = Form()

        form.display_form()
        formInput = form.get_result()
        scrapper = Scrapper(formInput)


App().main()
