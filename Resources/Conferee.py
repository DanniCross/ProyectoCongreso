from pygame import Rect


# Class for create the conferee object.
class Conferee:

    def __init__(self, party, id, name):
        self.left = None
        self.center = None
        self.right = None
        self.parent = None
        self.party = party
        self.id = id
        self.name = name
        self.x = 0
        self.y = 0
        self.outside = False # This parameter indicate if the node exceeds or not the maximun number of children.
        self.adjacent = []
        self.rect = Rect(0, 0, 30, 30)
        self.level = 0
