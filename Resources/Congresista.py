from Base.Base import Base


class Congresista(Base):

    def __init__(self, left, center, right, party, idpos, id, posx, posy):
        Base.__init__(self, posx, posy)
        self.left = left
        self.center = center
        self.right = right
        self.party = party
        self.idpos = idpos
        self.id = id
