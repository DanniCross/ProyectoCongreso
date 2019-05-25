from GUI.GUI import GUI
from Json.JSONP import JSON


def main():
    json = JSON() 
    congress = json.Read() # Called the json reading method to insert the data in the tree
    GUI(congress) # Called the GUI, passing him the class with the tree 

main()
