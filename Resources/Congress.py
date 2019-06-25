from .Conferee import Conferee
from .Connection import Connection
import pygame
from time import sleep


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
        self.meet = []
        self.changeTwo = []
        self.added = []
        self.Full = False
        self.Complete = False
        self.ready = False
        self.ready1 = False
        self.way = []
        self.wait = True

    # This method allows add the root and new nodes to the tree.
    def add(self, parent, party, id, name):
        newconferee = Conferee(party, id, name)
        if self.root is None:
            self.root = newconferee
            self.root.self = Conferee(party, id, name)
        else:
            self.max += 1
            newconferee.id = self.max
            self.root = self.addNode(self.root, parent, newconferee)
            self.set_position(self.root, 0, None, 0)
            self.root = self.level(self.root, 0)
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
                actual.left.self = Conferee(conferee.party, conferee.id, conferee.name)
            elif actual.center is None:
                actual.center = conferee
                actual.center.parent = actual
                actual.center.self = Conferee(
                    conferee.party, conferee.id, conferee.name)
            elif actual.right is None:
                actual.right = conferee
                actual.right.parent = actual
                actual.right.self = Conferee(
                    conferee.party, conferee.id, conferee.name)
            else:
                actual.outside = True
            return actual
        actual.left = self.addNode(actual.left, parent, conferee)
        actual.center = self.addNode(actual.center, parent, conferee)
        actual.right = self.addNode(actual.right, parent, conferee)
        return actual

    def delete(self, conferee, parent):
        self.connections.clear()
        self.levelMax = 0
        self.max = 0
        self.height = 0
        self.weight = 0
        self.Type = ""
        self.Full = False
        self.Complete = False
        self.way = []
        self.root = self.deleteNode(conferee, parent)
        self.set_position(self.root, 0, None, 0)
        self.root = self.level(self.root, 0)
        self.TypeDef()
        way = [self.root.id]
        self.longer_way(self.root, way)
        return self

    def deleteNode(self, conferee, parent):
        if conferee is None or parent is None:
            return
        if parent is conferee:
            if conferee.left is conferee.center is conferee.right is None:
                parent.parent = None
                parent = None
                return parent
            elif parent.left is parent.center is None and parent.right is not None:
                parent = self.deletebranch1(parent, parent.right)
                return parent
            elif parent.left is parent.right is None and parent.center is not None:
                parent = self.deletebranch1(parent, parent.center)
                return parent
            elif parent.right is parent.center is None and parent.left is not None:
                parent = self.deletebranch1(parent, parent.left)
                return parent
            elif parent.left is None and parent.center is not None and parent.right is not None:
                parent = self.deletebranch2(parent, parent.center)
                return parent
            elif parent.center is None and parent.left is not None and parent.right is not None:
                parent = self.deletebranch2(parent, parent.left)
                return parent
            elif parent.right is None and parent.left is not None and parent.center is not None:
                parent = self.deletebranch2(parent, parent.left)
                return parent
            elif parent.right is not None and parent.left is not None and parent.center is not None:
                parent = self.deletebranch3(parent, parent.left)
                return parent
        parent.left = self.deleteNode(conferee, parent.left)
        parent.center = self.deleteNode(conferee, parent.center)
        parent.right = self.deleteNode(conferee, parent.right)
        return parent

    def deletebranch1(self, parent, node):
        if node is None:
            return None
        node.parent = parent.parent
        parent = node
        return parent

    def deletebranch2(self, parent, node):
        if node is None:
            return None
        if node.left is node.center is node.right is None:
            if parent.center is node:
                node.left = parent.left
            else:
                node.center = parent.center
            node.right = parent.right
            parent = node
        elif node.left is not None and node.center is node.right is None:
            if parent.left is node:
                node.center = parent.center
            node.right = parent.right
            parent = node
        elif node.center is not None and node.left is node.right is None:
            if parent.center is node or parent.center is None:
                node.left = parent.left
                node.right = parent.right
                parent = node
            elif parent.center is not None:
                node.left = node.center
                node.center = parent.center
                node.right = parent.right
                node.center = None
                parent = node
        elif node.right is not None and node.left is node.center is None:
            if parent.right is not None:
                node.center = node.right
                node.right = parent.right
                parent = node
            elif parent.center is node:
                node.left = parent.left
            else:
                node.center = parent.center
            parent = node
        elif node.left is not None and node.center is not None and node.right is None:
            if parent.center is not None and parent.left is node:
                node.right = node.center
                node.center = parent.center
                parent = node
            else:
                node.right = parent.right
                parent = node
        elif node.left is not None and node.right is not None and node.center is None:
            if parent.right is not None:
                node.center = node.right
                node.right = parent.right
                parent = node
            else:
                node.center = parent.center
                parent = node
        elif node.left is None and node.center is not None and node.right is not None:
            if parent.left is node and parent.center is not None:
                node.left = node.center
                node.center = parent.center
                parent = node
            else:
                node.left = node.center
                node.center = node.right
                node.right = parent.right
                parent = node
        elif node.left is not None and node.center is not None and node.right is not None:
            temp = Conferee(node.party, node.id, node.name)
            temp.parent = node.parent
            temp.outside = node.outside
            temp.level = node.level
            temp.left = parent.left
            temp.center = parent.center
            temp.right = parent.right
            parent = temp
            parent = self.deleteNode(parent.left, parent)
        return parent

    def deletebranch3(self, parent, node):
        if node is None:
            return

        if node.left is node.center is node.right is None:
            node.center = parent.center
            node.right = parent.right
            parent = node

        elif node.left is not None and node.center is node.right is None:
            node.center = parent.center
            node.right = parent.right
            parent = node

        elif node.center is not None and node.left is node.right is None:
            node.left = node.center
            node.center = parent.center
            node.right = parent.right
            parent = node

        elif node.right is not None and node.left is node.center is None:
            node.left = node.right
            node.center = parent.center
            node.right = parent.right
            parent = node

        elif node.left is not None and node.center is not None and node.right is None:
            if parent.center.left is parent.center.center is parent.center.right is None:
                parent.center.left = node.left
                parent.center.center = node.center
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.left is not None and parent.center.center is parent.center.right is None:
                parent.center.right = parent.center.left
                parent.center.left = node.left
                parent.center.center = node.center
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.center is not None and parent.center.left is parent.center.right is None:
                parent.center.right = parent.center.center
                parent.center.left = node.left
                parent.center.center = node.center
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.right is not None and parent.center.left is parent.center.center is None:
                parent.center.left = node.left
                parent.center.center = node.center
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            else:
                temp = Conferee(node.party, node.id, node.name)
                temp.parent = node.parent
                temp.outside = node.outside
                temp.level = node.level
                temp.left = parent.left
                temp.center = parent.center
                temp.right = parent.right
                parent = temp
                parent = self.deleteNode(parent.left, parent)

        elif node.left is not None and node.right is not None and node.center is None:
            if parent.center.left is parent.center.center is parent.center.right is None:
                parent.center.left = node.left
                parent.center.right = node.right
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.left is not None and parent.center.center is parent.center.right is None:
                parent.center.center = parent.center.left
                parent.center.left = node.left
                parent.center.right = node.right
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.center is not None and parent.center.left is parent.center.right is None:
                parent.center.left = node.left
                parent.center.right = node.right
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.right is not None and parent.center.left is parent.center.center is None:
                parent.center.left = node.left
                parent.center.center = node.right
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            else:
                temp = Conferee(node.party, node.id, node.name)
                temp.parent = node.parent
                temp.outside = node.outside
                temp.level = node.level
                temp.left = parent.left
                temp.center = parent.center
                temp.right = parent.right
                parent = temp
                parent = self.deleteNode(parent.left, parent)

        elif node.center is not None and node.right is not None and node.left is None:
            if parent.center.left is parent.center.center is parent.center.right is None:
                parent.center.center = node.center
                parent.center.right = node.right
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.left is not None and parent.center.center is parent.center.right is None:
                parent.center.center = node.center
                parent.center.right = node.right
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.center is not None and parent.center.left is parent.center.right is None:
                parent.center.left = node.center
                parent.center.right = parent.center.center
                parent.center.center = node.right
                node.center = parent.center
                node.right = parent.right
                parent = node
            elif parent.center.right is not None and parent.center.left is parent.center.center is None:
                parent.center.left = node.center
                parent.center.center = node.right
                node.center = parent.center
                node.right = parent.right
                parent = node
            else:
                temp = Conferee(node.party, node.id, node.name)
                temp.parent = node.parent
                temp.outside = node.outside
                temp.level = node.level
                temp.left = parent.left
                temp.center = parent.center
                temp.right = parent.right
                parent = temp
                parent = self.deleteNode(parent.center, parent)
        else:
            if parent.center.left is parent.center.center is parent.center.right is None:
                parent.center.left = node.left
                parent.center.center = node.center
                parent.center.right = node.right
                node.left = None
                node.center = parent.center
                node.right = parent.right
                parent = node
            else:
                temp = Conferee(node.party, node.id, node.name)
                temp.parent = node.parent
                temp.outside = node.outside
                temp.level = node.level
                temp.left = parent.left
                temp.center = parent.center
                temp.right = parent.right
                parent = temp
                parent = self.deleteNode(parent.left,  parent)
        return parent

    def change(self, parent, node, id, name):
        self.root = self.ChangeId(parent, node, id, name)
        self.way = []
        way = [self.root.id]
        self.longer_way(self.root, way)
        return self.root

    def ChangeId(self, parent, node, id, name):
        if parent is None or node is None:
            return
        if parent is node:
            parent.id = id
            parent.name = name
            return parent
        parent.left = self.ChangeId(parent.left, node, id, name)
        parent.center = self.ChangeId(parent.center, node, id, name)
        parent.right = self.ChangeId(parent.right, node, id, name)
        return parent
    
    def Meet(self, leader):
        leaderT = Conferee(leader.party, leader.id, leader.name)
        self.meet.clear()
        self.ready = False
        self.ready1 = False
        self.changeTwo.clear()
        self.SMembers(self.root, leaderT)
        pas = True
        i = 0
        while pas:
            self.root = self.Meeting(self.root, leaderT, self.meet[i])
            if self.ready:
                self.meet.clear()
                self.SMembers(self.root, leaderT)
                i = -1
            if i == len(self.meet) - 1:
                self.meet.clear()
            if len(self.meet) == 0:
                pas = False
            self.ready = False
            self.ready1 = False
            i += 1

        for conferee in self.changeTwo:
            self.root = self.EndChange(self.root, conferee)
        self.connections.clear()
        self.levelMax = 0
        self.max = 0
        self.height = 0
        self.weight = 0
        self.Type = ""
        self.Full = False
        self.Complete = False
        self.way = []
        self.set_position(self.root, 0, None, 0)
        self.root = self.level(self.root, 0)
        self.TypeDef()
        way = [self.root.id]
        self.longer_way(self.root, way)
        return self

    def EndChange(self, parent, node):
        if parent is None:
            return
        if parent is node.new:
            iden = node.id
            name = node.name
            party = node.party
            parent.id = iden
            parent.name = name
            parent.party = party
            return parent
        parent.left = self.EndChange(parent.left, node)
        parent.center = self.EndChange(parent.center, node)
        parent.right = self.EndChange(parent.right, node)
        return parent

    def Meeting(self, parent, leader, node):
        if parent is None:
            return
        if parent.left is not None and parent.left.id is leader.id and not self.ready1:
            if self.searchSpaces(parent.left, leader.party, False):
                parent.left = self.changeParty(parent.left, leader.party, node)
            else:
                iden1 = parent.id
                name1 = parent.name
                party1 = parent.party
                parent1 = parent.parent
                iden2 = parent.left.id
                name2 = parent.left.name
                party2 = parent.left.party
                parent2 = parent.left.parent
                parent.id = iden2
                parent.name = name2
                parent.parent = parent2
                parent.party = party2
                parent.left.id = iden1
                parent.left.name = name1
                parent.left.parent = parent1
                parent.left.party = party1
                self.ready = True
            return parent
        elif parent.center is not None and parent.center.id is leader.id and not self.ready1:
            if self.searchSpaces(parent.center, leader.party, False):
                parent.center = self.changeParty(parent.center, leader.party, node)
            else:
                iden1 = parent.id
                name1 = parent.name
                party1 = parent.party
                parent1 = parent.parent
                iden2 = parent.center.id
                name2 = parent.center.name
                party2 = parent.center.party
                parent2 = parent.center.parent
                parent.id = iden2
                parent.name = name2
                parent.parent = parent2
                parent.party = party2
                parent.center.id = iden1
                parent.center.name = name1
                parent.center.parent = parent1
                parent.center.party = party1
                self.ready = True
            return parent
        elif parent.right is not None and parent.right.id is leader.id and not self.ready1:
            if self.searchSpaces(parent.right, leader.party, False):
                parent.right = self.changeParty(parent.right, leader.party, node)
            else:
                iden1 = parent.id
                name1 = parent.name
                party1 = parent.party
                parent1 = parent.parent
                iden2 = parent.right.id
                name2 = parent.right.name
                party2 = parent.right.party
                parent2 = parent.right.parent
                parent.id = iden2
                parent.name = name2
                parent.parent = parent2
                parent.party = party2
                parent.right.id = iden1
                parent.right.name = name1
                parent.right.parent = parent1
                parent.right.party = party1
                self.ready = True
            return parent
        parent.left = self.Meeting(parent.left, leader, node)
        if self.ready or self.ready1:
            return parent
        parent.center = self.Meeting(parent.center, leader, node)
        if self.ready or self.ready1:
            return parent
        parent.right = self.Meeting(parent.right, leader, node)
        if self.ready or self.ready1:
            return parent
        return parent
        
    def changeParty(self, parent, party, node):
        if parent is None:
            return
        if parent.party is not party and not self.ready1:
            temp = Conferee(parent.party, parent.id, parent.name)
            iden = node.id
            name = node.name
            party = node.party
            parent.id = iden
            parent.name = name
            parent.party = party
            temp.new = node
            self.changeTwo.append(temp)
            self.ready1 = True
            self.added.append(node)
            return parent
        parent.left = self.changeParty(parent.left, party, node)
        parent.center = self.changeParty(parent.center, party, node)
        parent.right = self.changeParty(parent.right, party, node)
        return parent

    def searchSpaces(self, parent, party, space):
        if parent is None:
            return space
        if parent.party is not party:
            space = True
            return space
        space = self.searchSpaces(parent.left, party, space)
        space = self.searchSpaces(parent.center, party, space)
        space = self.searchSpaces(parent.right, party, space)
        return space
    
    def SMembers(self, parent, leader):
        if parent is None:
            return
        if parent.party is leader.party and parent not in self.added:
            self.meet.append(parent)
        if parent.left is not None and parent.left.id is not leader.id:
            self.SMembers(parent.left, leader)
        if parent.center is not None and parent.center.id is not leader.id:
            self.SMembers(parent.center, leader)
        if parent.right is not None and parent.right.id is not leader.id:
            self.SMembers(parent.right, leader)
    
    def reset(self):
        self.meet.clear()
        self.ready = False
        self.ready1 = False
        self.changeTwo.clear()
        self.root = self.__reset(self.root)
        self.connections.clear()
        self.levelMax = 0
        self.max = 0
        self.height = 0
        self.weight = 0
        self.Type = ""
        self.Full = False
        self.Complete = False
        self.way = []
        self.set_position(self.root, 0, None, 0)
        self.root = self.level(self.root, 0)
        self.TypeDef()
        way = [self.root.id]
        self.longer_way(self.root, way)
        return self

    def __reset(self, parent):
        if parent is None:
            return
        parent.id = parent.self.id
        parent.name = parent.self.name
        parent.party = parent.self.party
        parent.left = self.__reset(parent.left)
        parent.center = self.__reset(parent.center)
        parent.right = self.__reset(parent.right)
        return parent


    # This methos give the connections between the nodes.
    def addConnection(self, c1, c2):
        if c2 is None:
            return
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
        if parent.left is not None:
            parent.left.parent = parent
            self.addConnection(parent, parent.left)
        if parent.center is not None:
            parent.center.parent = parent
            self.addConnection(parent, parent.center)
        if parent.right is not None:
            parent.right.parent = parent
            self.addConnection(parent, parent.right)
        parent.left = self.level(parent.left, i + 1)
        parent.center = self.level(parent.center, i + 1)
        parent.right = self.level(parent.right, i + 1)
        return parent

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

    def width(self, conferees, screen, time):
        if len(conferees) == 0:
            return
        pygame.draw.circle(screen, (255, 255, 255),
                           (conferees[0].x + 15, conferees[0].y + 10), 15, 15)
        pygame.display.update()
        sleep(time)
        if conferees[0].left is not None:
            conferees.append(conferees[0].left)
        if conferees[0].center is not None:
            conferees.append(conferees[0].center)
        if conferees[0].right is not None:
            conferees.append(conferees[0].right)
        conferees.remove(conferees[0])
        self.width(conferees, screen, time)

    def preorder(self, parent, screen, time):
        if parent is None:
            return
        pygame.draw.circle(screen, (255, 255, 255),
                           (parent.x + 15, parent.y + 10), 15, 15)
        pygame.display.update()
        sleep(time)
        self.preorder(parent.left, screen, time)
        self.preorder(parent.center, screen, time)
        self.preorder(parent.right, screen, time)

    def inorder(self, parent, screen, time):
        if parent is None:
            return
        self.inorder(parent.left, screen, time)
        pygame.draw.circle(screen, (255, 255, 255),
                           (parent.x + 15, parent.y + 10), 15, 15)
        pygame.display.update()
        sleep(time)
        self.inorder(parent.center, screen, time)
        self.inorder(parent.right, screen, time)

    def posorder(self, parent, screen, time):
        if parent is None:
            return
        self.posorder(parent.left, screen, time)
        self.posorder(parent.center, screen, time)
        self.posorder(parent.right, screen, time)
        pygame.draw.circle(screen, (255, 255, 255),
                           (parent.x + 15, parent.y + 10), 15, 15)
        pygame.display.update()
        sleep(time)

    def TypeDef(self):
        conferees = [self.root]
        Type = self.__Type(conferees)
        if Type is "FULL":
            self.Full = True
            self.Complete = True
        elif Type is "COMPLETE":
            self.Full = False
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
