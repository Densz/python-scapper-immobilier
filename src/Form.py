from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json


class Form:
    def __init__(self):
        # Dictionaries
        self.__formResult = {
            'website': '',
            'department': '',
            'budget': '',
        }

    def __ask_website(self):
        options = ['All', 'SeLoger', 'LeBonCoin']
        question = {
            'type': 'list',
            'name': 'website',
            'message': 'Select website to scrap',
            'choices': options
        }
        return prompt(question)['website']

    def __ask_department(self):
        question = {
            'type': 'input',
            'name': 'department',
            'message': 'Please enter the department (eg: 75011):'
        }
        return prompt(question)['department']

    def __ask_budget_limit(self):
        question = {
            'type': 'input',
            'name': 'budget',
            'message': 'What is your budget:'
        }
        return prompt(question)['budget']

    def display_form(self):
        self.__formResult = {
            'website': self.__ask_website(),
            'department': self.__ask_department(),
            'budget': self.__ask_budget_limit(),
        }

    def get_result(self):
        return self.__formResult
