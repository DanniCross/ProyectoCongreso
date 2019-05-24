from Resources.Congress import Congress
from random import randint
import json


class JSON2:
    def __init__(self):
        self.congress = Congress()

    def Read(self):
        with open("Json/names.json") as file:
            data = json.load(file)

        num = randint(1, 10)
        for item in data['items']:
            if item['id'] == num:
                return item['name']
