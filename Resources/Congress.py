from .Conferee import Conferee
from .Connection import Connection


# Class where the tree is created.
class Congress:

    def __init__(self):
        self.root = None
        self.max = 0
        self.parties = []
        self.connections = []
        self.levelMax = 0
        self.height = 0
        self.weight = 0
        self.Type = ""
        self.Full = False
        self.Complete = False
        self.way = []

    # This method allows add the root and new nodes to the tree.
    def add(self, parent, party, id, name):
        newconferee = Conferee(party, id, name)
        if self.root is None:
            self.root = newconferee
        else:
            self.max += 1
            newconferee.id = self.max
            self.root = self.addNode(self.root, parent, newconferee)
            self.set_position(self.root, 0, None, 0)
            self.level(self.root, 0)
            self.weight += 1
            self.TypeDef()
            way = [self.root.id]
            self.longer_way(self.root, way)

    # With this method the new nodes are added in one position (left, center or right).
    def addNode(self, actual, parent, conferee):
        if actual is None:
            return actual
        if actual == parent:
            if actual.left is None:
                actual.left = conferee
                actual.left.parent = actual
                self.addConnection(actual, actual.left)
            elif actual.center is None:
                actual.center = conferee
                actual.center.parent = actual
                self.addConnection(actual, actual.center)
            elif actual.right is None:
                actual.right = conferee
                actual.right.parent = actual
                self.addConnection(actual, actual.right)
            else:
                actual.outside = True
            return actual
        actual.left = self.addNode(actual.left, parent, conferee)
        actual.center = self.addNode(actual.center, parent, conferee)
        actual.right = self.addNode(actual.right, parent, conferee)
        return actual

    # TODO
    def deleteNode(self, conferee):
        if conferee != none:
            return self.__deleteNode(self.root, conferee)
        else:
            return False

    def __deleteNode(self, node, conferee):
        if node == None:
            return False
        if node.left != None and node.left == conferee:
            pass
        elif node.center != None and node.center == conferee:
            pass
        else:
            pass
        state = self.__deleteNode(node.left, conferee)
        if state != True:
            state = self.__deleteNode(node.center, conferee)
            if state != True:
                state = self.__deleteNode(node.right, conferee)
        return state

    # This methos give the connections between the nodes.
    def addConnection(self, c1, c2):
        conect = Connection(c1, c2)
        conAux = Connection(c2, c1)
        if conect in self.connections or conAux in self.connections:
            return
        self.connections.append(conect)
        c1.adjacent.append(c2)
        c2.adjacent.append(c1)

    # With this method the screen position of each node is given.
    def set_position(self, current, i, previous, j):
        if current is not None:
            if i == 0:
                current.x = 660
                current.y = 10
                current.rect.x = current.x
                current.rect.y = current.y
                previous = current
            elif i == 1:
                current.x = previous.x - (320 - j)
                current.y = previous.y + 100
                current.rect.x = current.x
                current.rect.y = current.y
                previous = current
            elif i == 2:
                current.x = previous.x
                current.y = previous.y + 100
                current.rect.x = current.x
                current.rect.y = current.y
                previous = current
            else:
                current.x = previous.x + (320 - j)
                current.y = previous.y + 100
                current.rect.x = current.x
                current.rect.y = current.y
                previous = current
            self.set_position(current.left, 1, previous, j + 70)
            self.set_position(current.center, 2, previous, j + 70)
            self.set_position(current.right, 3, previous, j + 70)
    
    # This method allows calculate the level and the height of the tree.
    def level(self, parent, i):
        if parent is None:
            return
        parent.level = i
        if parent.level >= self.levelMax:
            self.levelMax = parent.level + 1
            self.height = self.levelMax
        self.level(parent.left, i + 1)
        self.level(parent.center, i + 1)
        self.level(parent.right, i + 1)
    
    def Tours(self):
        conferees = [self.root]
        print("*Width")
        self.__width(conferees)
        print("\n\n*Preorder")
        self.__preorder(self.root)
        print("\n\n*Inorder")
        self.__inorder(self.root)
        print("\n\n*Posorder")
        self.__posorder(self.root)
    
    def __width(self, conferees):
        if len(conferees) == 0:
            return
        print(f" - {conferees[0].name}", end="")
        if conferees[0].left is not None:
            conferees.append(conferees[0].left)
        if conferees[0].center is not None:
            conferees.append(conferees[0].center)
        if conferees[0].right is not None:
            conferees.append(conferees[0].right)
        conferees.remove(conferees[0])
        self.__width(conferees)
    
    def __preorder(self, parent):
        if parent is None:
            return
        print(f" - {parent.name}", end="")
        self.__preorder(parent.left)
        self.__preorder(parent.center)
        self.__preorder(parent.right)

    def __inorder(self, parent):
        if parent is None:
            return
        self.__preorder(parent.left)
        print(f" - {parent.name}", end="")
        self.__preorder(parent.center)
        self.__preorder(parent.right)

    def __posorder(self, parent):
        if parent is None:
            return
        self.__preorder(parent.left)
        self.__preorder(parent.right)
        self.__preorder(parent.center)
        print(f" - {parent.name}", end="")

    def TypeDef(self):
        conferees = [self.root]
        Type = self.__Type(conferees)
        if Type is "FULL":
            self.Full = True
            self.Complete = True
        elif Type is "COMPLETE":
            self.Complete = True

    def __Type(self, conferees):
        if len(conferees) == 0:
            return "FULL"
        if conferees[0].level is (self.levelMax - 2):
            if conferees[0].left is None or conferees[0].center is None or conferees[0].right is None:
                return "COMPLETE"
        if (conferees[0].level is not (self.levelMax - 1) and 
            (conferees[0].left is None or conferees[0].center is None or conferees[0].right is None)):
            return "NO"
        if conferees[0].level is not (self.levelMax - 1):
            conferees.append(conferees[0].left)
            conferees.append(conferees[0].center)
            conferees.append(conferees[0].right)
        conferees.remove(conferees[0])
        return self.__Type(conferees)
            
    def longer_way(self, parent, current):
        if parent is None:
            return
        if parent is not self.root:
            for i in range((len(current) - 1), -1, -1):
                if parent.parent.id is current[i]:
                    break
                current.remove(current[i])
            current.append(parent.id)
        if len(self.way) < len(current):
            self.way.clear()
            for confer in current:
                self.way.append(confer)
        self.longer_way(parent.left, current)
        self.longer_way(parent.center, current)
        self.longer_way(parent.right, current)
        
