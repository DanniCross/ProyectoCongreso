from GUI.GUI import GUI
from Json.JSONP import JSON


def main():
    json = JSON()
    congress = json.Read()
    GUI(congress)


main()
