from Base.Base import Base


class Conferee(Base):

    def __init__(self, party, idpos, id, name, posx, posy):
        Base.__init__(self, posx, posy)
        self.left = None
        self.center = None
        self.right = None
        self.party = party
        self.idpos = idpos
        self.id = id
        self.name = name
