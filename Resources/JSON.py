from .Congress import Congress
from .Conferee import Conferee
from .Party import Party
import json

class JSON:
    
    def __init__(self):
        self.color = None
    
    def Read(self):
        congress = Congress()
        with open("/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/ProyectoI/format.json") as file:
            data = json.load(file)
        
        name = data['president']['name']
        congress.add(0, 0, name)
        for party in data['party']:
            color = party['color']
            if color == "red":
                self.color = (255, 0, 0)
            elif color == "blue":
                self.color = (0, 255, 0)
            elif color == "green":
                self.color = (0, 0, 255)
            else:
                self.color = (255, 255, 0)
            par = Party(int(party['id']), party['name'], int(party['leader']), self.color)
            congress.parties.append(par)
        congress.root = self.CreateConf(congress.root, data['people'])
        return congress.root
    
    def CreateConf(self, parent, data):
        for conferee in data: 
            if parent.left is None:
                parent.left = Conferee(int(conferee['party']), 0, int(conferee['id']), conferee['name'], 0, 0)
                if len(conferee['childrens']) > 0:
                    parent.left = self.CreateConf(parent.left, conferee['childrens'])
                    continue
                continue
            if parent.center is None:
                parent.center = Conferee(int(conferee['party']), 0, int(conferee['id']), conferee['name'], 0, 0)
                if len(conferee['childrens']) > 0:
                    parent.center = self.CreateConf(parent.center, conferee['childrens'])
                    continue
                continue
            if parent.right is None:
                parent.right = Conferee(int(conferee['party']), 0, int(conferee['id']), conferee['name'], 0, 0)
                if len(conferee['childrens']) > 0:
                    parent.right = self.CreateConf(parent.right, conferee['childrens'])
                    continue
                continue
        return parent
