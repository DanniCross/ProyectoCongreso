import pygame
import random
import string
from Estructura.barrio import Barrio


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
        ventana.blit(agregar, (self.x + 10, self.y + 20))

    def agregar(self, ciudad):
        if self is not ciudad:
            grafo = ciudad
            id = "Barrio " + random.choice(string.ascii_uppercase)
            pas = False
            i = 0
            x = random.randint(250, 1200)
            y = random.randint(60, 600)
            if len(ciudad.barrios) > 0:
                while i in range(len(ciudad.barrios)):
                    if len(ciudad.barrios) == 20:
                        print("No se pueden añadir mas nodos")
                        break
                    else:
                        if id != ciudad.barrios[i].id:
                            if pas is not True:
                                pas = True
                            if i == len(ciudad.barrios) - 1:
                                while self.sobrepos(x, y, ciudad):
                                    x = random.randint(250, 1200)
                                    y = random.randint(60, 600)
                        else:
                            id = "Barrio " + random.choice(string.ascii_uppercase)
                            i = -1
                            if pas is not False:
                                pas = False
                    i += 1
            else:
                ciudad.agregarBarrio(
                    id, x, y, random.randint(0, 1), random.randint(1, 300)
                )
            if pas is True:
                ciudad.agregarBarrio(
                    id, x, y, random.randint(0, 1), random.randint(1, 300)
                )
                n = random.randint(0, len(ciudad.barrios) - 1)
                while pas:
                    if ciudad.barrios[n].id != id:
                        pas = False
                    else:
                        n = random.randint(0, len(ciudad.barrios) - 1)
                ciudad.agregarTuberia(
                    ciudad.buscarBarrio(id),
                    ciudad.buscarBarrio(ciudad.barrios[n].id),
                    random.randint(1, 5),
                )
            return ciudad

    def sobrepos(self, x, y, ciudad):
        if self is not ciudad:
            for br in ciudad.barrios:
                if br.x >= x - 100 and br.y >= y - 100:
                    if br.x <= x + 100 and br.y <= y + 100:
                        return True
            return False

