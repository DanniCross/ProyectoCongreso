from Resources.Congress import Congress
from Resources.Conferee import Conferee
from Resources.Party import Party
import json


class JSON:

    def __init__(self):
        self.color = None
        self.congress = Congress()

    def Read(self):
        with open("Json/format.json") as file:
            data = json.load(file)

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
            par = Party(int(party['id']), party['name'],
                        int(party['leader']), self.color)
            self.congress.parties.append(par)
        self.congress.root = self.CreateConf(
            self.congress.root, data['people'])
        self.congress.set_position(self.congress.root, 0, None, 0)
        self.congress.level(self.congress.root, 0)
        return self.congress

    def CreateConf(self, parent, data):
        for conferee in data:

            if parent is None:
                self.congress.add(None, int(conferee['party']), int(conferee['id']), conferee['name'])
                if int(conferee['id']) > self.congress.max:
                    self.congress.max = int(conferee['id'])
                parent = self.CreateConf(self.congress.root, conferee['childrens'])

            if parent.left is None:
                parent.left = Conferee(int(conferee['party']), int(conferee['id']), conferee['name'])
                self.congress.addConnection(parent, parent.left)
                if parent.left.id > self.congress.max:
                    self.congress.max = parent.left.id
                if 0 < len(conferee['childrens']):
                    if len(conferee['childrens']) > 3:
                        parent.left.outside = True
                    parent.left = self.CreateConf(parent.left, conferee['childrens'])
                    continue
                continue

            if parent.center is None:
                parent.center = Conferee(int(conferee['party']), int(conferee['id']), conferee['name'])
                self.congress.addConnection(parent, parent.center)
                if parent.center.id > self.congress.max:
                    self.congress.max = parent.center.id
                if 0 < len(conferee['childrens']):
                    if len(conferee['childrens']) > 3:
                        parent.center.outside = True
                    parent.center = self.CreateConf(parent.center, conferee['childrens'])
                    continue
                continue

            if parent.right is None:
                parent.right = Conferee(int(conferee['party']), int(conferee['id']), conferee['name'])
                self.congress.addConnection(parent, parent.right)
                if parent.right.id > self.congress.max:
                    self.congress.max = parent.right.id
                if 0 < len(conferee['childrens']):
                    if len(conferee['childrens']) > 3:
                        parent.right.outside = True
                    parent.right = self.CreateConf(parent.right, conferee['childrens'])
                    continue
                continue

        return parent