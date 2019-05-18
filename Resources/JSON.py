from Congress import Congress
from Conferee import Conferee
from Party import Party

class JSON:
    
    def Read(self):
        with open('format.json') as file:
            data = json.load(file)
        
        Congress.add(0, 0, data['president']['name'])
        for party in data['party']:
            par = Party(party['id'], party['name'], party['leader'], party['color'])
            Congress.parties.append(par)
        Congress.root = self.CreateConf(Congress.root, data['people'])
    
    def CreateConf(self, parent, data):
        for conferee in data: 
            if parent.left is None:
                parent.left(Conferee(conferee['party'], 0, conferee['id'], conferee['name'], 0, 0))
                if len(conferee['childrens']) > 0:
                    parent.left = self.CreateConf(parent.left, conferee['childrens'])
                    continue
                continue
            if parent.center is None:
                parent.center(Conferee(conferee['party'], 0, conferee['id'], conferee['name'], 0, 0))
                if len(conferee['childrens']) > 0:
                    parent.center = self.CreateConf(parent.center, conferee['childrens'])
                    continue
                continue
            if parent.right is None:
                parent.right(Conferee(conferee['party'], 0, conferee['id'], conferee['name'], 0, 0))
                if len(conferee['childrens']) > 0:
                    parent.right = self.CreateConf(parent.right, conferee['childrens'])
                    continue
                continue
        return parent