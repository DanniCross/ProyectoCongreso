import pygame
import sys
import subprocess
from Views.button import Boton
from Views.cursor import Cursor
from random import randint
from tkinter import *
from tkinter import messagebox as mb
pygame.init()


class GUI:

    def __init__(self, congress):
        self.congress = congress
        self.font = None
        self.cursor = Cursor()
        self.draw()

    def screen_size(self):
        size = (None, None)
        args = ["xrandr", "-q", "-d", ":0"]
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
                if "Screen" in line:
                    size = (int(line.split()[7]), int(line.split()[9][:-1]))
        return size

    def draw(self):
        cursor = Cursor()
        screen = pygame.display.set_mode(self.screen_size())
        pygame.display.set_caption("Congress")

        # fonts
        self.font = pygame.font.SysFont("Arial Narrow", 20)
        add = self.font.render("Add Node", True, (255, 255, 255))

        # Load images
        Red = pygame.image.load("Imgs/red.png")
        Blue = pygame.image.load("Imgs/blue.png")
        Yellow = pygame.image.load("Imgs/yellow.png")
        Green = pygame.image.load("Imgs/green.png")
        buttonUp = pygame.image.load("Imgs/ButtonUp.png")
        buttonDown = pygame.image.load("Imgs/ButtonDown.png")

        # Transform Images
        Red = pygame.transform.scale(Red, (30, 30))
        Blue = pygame.transform.scale(Blue, (30, 30))
        Yellow = pygame.transform.scale(Yellow, (30, 30))
        Green = pygame.transform.scale(Green, (30, 30))

        # buttons
        buttonAdd = Boton(buttonUp, buttonDown, 100, 650)
        buttonDelete = Boton(buttonUp, buttonDown, 200, 650)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cursor.colliderect(buttonAdd.rect):
                        buttonAdd.add(self.congress, randint(
                            1, 4), randint(1, 30), "jose")
                    elif cursor.colliderect(buttonAdd.rect):
                        buttonDelete.delete(self.congress, randint(1, 30))
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((125, 70, 200))
            self.draw_conect(screen, self.congress.connections)
            self.draw_congress(screen, self.congress.root, Red, Blue, Green, Yellow)

            cursor.update()
            buttonAdd.update(screen, cursor, add)
            pygame.display.update()

    def draw_congress(self, screen, parent, Red, Blue, Green, Yellow):
        if parent is None:
            return
        if parent.party == 1:
            screen.blit(Red, (parent.x, parent.y))
            screen.blit((self.font.render(
                f"  {parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x - 20, parent.y + 30))
        elif parent.party == 2:
            screen.blit(Blue, (parent.x, parent.y))
            screen.blit((self.font.render(
                f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x - 20, parent.y + 30))
        elif parent.party == 3:
            screen.blit(Green, (parent.x, parent.y))
            screen.blit((self.font.render(
                f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x - 20, parent.y + 30))
        elif parent.party == 4:
            screen.blit(Yellow, (parent.x, parent.y))
<<<<<<< HEAD
            screen.blit((self.fuente.render(
                f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x - 20, parent.y + 30))
=======
            screen.blit((self.font.render(f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x - 20, parent.y + 30))
>>>>>>> fca8541a0af0e20c358514edaedcadeeb8197a9c
        if parent.outside:
            parent.outside = False
            self.outside(parent)
        self.draw_congress(screen, parent.left, Red, Blue, Green, Yellow)
        self.draw_congress(screen, parent.center, Red, Blue, Green, Yellow)
        self.draw_congress(screen, parent.right, Red, Blue, Green, Yellow)

    def draw_conect(self, screen, connections):
        for conect in connections:
            pygame.draw.line(screen, (0, 0, 0), (conect.c1.x + 12,
                                                 conect.c1.y + 15), (conect.c2.x + 12, conect.c2.y + 15), 10)

    def outside(self, parent):
        screen = Tk()
        screen.withdraw()
        if mb.showinfo("ALERT", f"The conferee {parent.name} has above 3 political sons, so, only 3 will be added."):
            Tk().quit()
