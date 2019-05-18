from .Congresista import Congresista

class Congreso:

    def __init__(self, nodes, root):
        self.nodes = nodes
        self.root = root

    def add(self, ):
        newCongresista = Congresista()
        if self.root is None:
            self.root = newCongresista
        else:
            addNode()

    def addNode(self, parent):
        newCongresista = Congresista()
        if parent is None:
            parent = newCongresista

