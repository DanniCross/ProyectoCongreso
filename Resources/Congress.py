from .Conferee import Conferee


class Congress:

    def __init__(self):
        self.root = None
        self.parties = []

    def add(self, party, id, name):
        newconferee = Conferee(party, 0, id, name, 0, 0)
        if self.root is None:
            self.root = newconferee
        else:
            self.root = self.addNode(self.root, newconferee)

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

