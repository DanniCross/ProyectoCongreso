class Conferee():

    def __init__(self, party, idpos, id, name, x, y):
        self.left = None
        self.center = None
        self.right = None
        self.party = party
        self.idpos = idpos
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.outside = False
        self.adjacent = []
