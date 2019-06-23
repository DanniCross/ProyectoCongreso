import pygame

# Class that allows create a button in pygame.
class ButtonP(pygame.sprite.Sprite):

    def __init__(self, up, down, x, y):
        super(ButtonP, ButtonP).__init__(self)
        self.normal = up
        self.selection = down
        self.current = self.normal
        self.rect = self.current.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.x = x
        self.y = y

    # With this methos the button image is update according to the cursor position.
    def update(self, screen, cursor, add):
        if cursor.colliderect(self.rect):
            self.current = self.selection
        else:
            self.current = self.normal
        screen.blit(self.current, self.rect)
        screen.blit(add, (self.x + 10, self.y + 10))

    # methos for the add button.
    def add(self, congress, parent, party, id, name):
        congress.add(parent, party, id, name)

    # Method for the delete button.
    def delete(self, congress, parent):
        return congress.deleteNode(parent, congress.root)
    
    def verify_assitance(self, screen, congress, time, tour):
        if tour == 1:
            conferees = [congress.root]
            congress.width(conferees, screen, time)
        elif tour == 2:
            congress.preorder(congress.root, screen, time)
        elif tour == 3:
            congress.inorder(congress.root, screen, time)
        elif tour == 4:
            congress.posorder(congress.root, screen, time)
        
    def change(self, congress, parent, id, name):
        return congress.ChangeId(congress.root, parent, id, name)
