from .Congresista import Congresista


class Congreso:

    def __init__(self, nodes, root):
        self.nodes = nodes
        self.root = root

    def add(self, party, id):
        newCongresista = Congresista(None, None, None, party, 0, id, 0, 0)
        if self.root is None:
            self.root = newCongresista
        else:
            self.root = self.addNode(self.root, newCongresista)

    def addNode(self, parent, congresista):
        if parent is None:
            parent = congresista
            return parent
        elif congresista.id < parent.id:
            parent.left(self.addNode(parent.left, congresista))
        elif congresista.id == parent.id:
            parent.center(self.addNode(parent.center, congresista))
        else:
            parent.right(self.addNode(parent.right, congresista))
        return parent
