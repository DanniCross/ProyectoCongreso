from .Conferee import Conferee
from .Connection import Connection


class Congress:

    def __init__(self):
        self.root = None
        self.max = 0
        self.parties = []
        self.connections = []

    def add(self, party, id, name):
        newconferee = Conferee(party, 0, id, name, 0, 0)
        if self.root is None:
            self.root = newconferee
        else:
            self.root = self.addNode(self.root, newconferee)
            self.set_position(self.root, 0, None, 0)

    def addNode(self, parent, conferee):
        if parent is None:
            parent = conferee
            return parent
        elif conferee.id < parent.id:
            parent.left(self.addNode(parent.left, conferee))
        elif conferee.id == parent.id:
            parent.center(self.addNode(parent.center, conferee))
        else:
            parent.right(self.addNode(parent.right, conferee))
        return parent
    
    def addConnection(self, c1, c2):
        conect = Connection(c1, c2)
        conAux = Connection(c2, c1)
        if conect in self.connections or conAux in self.connections:
            return
        self.connections.append(conect)
        c1.adjacent.append(c2)
        c2.adjacent.append(c1)

    def set_position(self, current, i, previous, j):
        if current is not None:
            if i == 0:
                current.x = 660
                current.y = 10
                previous = current
            elif i == 1:
                current.x = previous.x - (320 - j)
                current.y = previous.y + 100
                previous = current
            elif i == 2:
                current.x = previous.x
                current.y = previous.y + 100
                previous = current
            else:
                current.x = previous.x + (320 - j)
                current.y = previous.y + 100
                previous = current
            self.set_position(current.left, 1, previous, j + 70)
            self.set_position(current.center, 2, previous, j + 70)
            self.set_position(current.right, 3, previous, j + 70)
                

