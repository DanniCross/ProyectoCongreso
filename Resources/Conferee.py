from pygame import Rect


class Conferee:

    def __init__(self, party, id, name):
        self.left = None
        self.center = None
        self.right = None
        self.party = party
        self.id = id
        self.name = name
        self.x = 0
        self.y = 0
        self.outside = False
        self.adjacent = []
        self.rect = Rect(0, 0, 30, 30)
        self.level = 0
