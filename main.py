from GUI.GUI import GUI
from Resources.JSON import JSON


def main():
    json = JSON()
    root = json.Read()
    GUI(root)
    
main()
