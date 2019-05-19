from GUI.GUI import GUI
from Resources.JSON import JSON


def main():
    json = JSON()
    congress = json.Read()
    GUI(congress)
    
main()
