import pygame
import random
import string
from Resources.Conferee import Conferee
from Resources.Congress import Congress


class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen, imagen1, x, y):
        super(Boton, Boton).__init__(self)
        self.normal = imagen
        self.seleccion = imagen1
        self.actual = self.normal
        self.rect = self.actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.x = x
        self.y = y

    def update(self, ventana, cursor, agregar):
        if cursor.colliderect(self.rect):
            self.actual = self.seleccion
        else:
            self.actual = self.normal
        ventana.blit(self.actual, self.rect)
        ventana.blit(agregar, (self.x + 10, self.y + 10))

    def add(self, congress, parent, party, id, name):
        congress.add(parent, party, id, name)

    def delete(self, congress):
        pass

