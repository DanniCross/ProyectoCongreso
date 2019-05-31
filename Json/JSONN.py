from random import randint
import json
import os


# Class for read a personal json file with some names for new nodes.
class JSON2:
    def __init__(self):
        self.file = ""

    def Read(self):
        if os.name is "posix":
            file = "Json/names.json"
        else:
            file = "Json\\names.json"

        with open(file) as jfile:
            data = json.load(jfile)

        # Random selection of a name.
        num = randint(1, 10)
        for item in data['items']:
            if item['id'] == num:
                return item['name']
