class Form:
    def __init__(self):
        # Dictionaries
        self.__formResult = {
            'website': '',
            'department': '',
            'budget': '',
        }

    def __ask_website(self):
        s = input("Select which website")
        self.__formResult['website'] = s
        return 1

    def __ask_department(self):
        return 0

    def __ask_budget_limit(self):
        return 0

    def get_form(self):
        self.__ask_website()
        self.__ask_department()
        self.__ask_budget_limit()

    def get_result(self):
        return self.__formResult
