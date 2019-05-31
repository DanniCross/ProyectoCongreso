import pygame
import subprocess
import os
import ctypes
from tkinter import *
from tkinter import messagebox as mb
from Views.cursor import Cursor
from Views.button import ButtonP
from random import randint
from Json.JSONN import JSON2
pygame.init() # Pygame initialization.


# Graphical user interface class.
class GUI:

    def __init__(self, congress):
        self.congress = congress # Entry of the congress class to the GUI init.
        self.font = None
        self.cursor = Cursor() # Called to the Cursor class for recognize the mouse with pygame.
        self.draw() # Called to the draw method where is the GUI code.
        self.son = False

    # Method that returns the screen size in Linux.
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
    
    def screen_sizeW(self):
        self.n = 0
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        size = (ancho, alto)
        return size

    def draw(self):
        json = JSON2()
        cursor = Cursor()
        if os.name is "posix":
            screen = pygame.display.set_mode(self.screen_size())  # Window size defnition.
        else:
            screen = pygame.display.set_mode(self.screen_sizeW(), pygame.RESIZABLE)
        pygame.display.set_caption("Congress")

        # fonts.
        self.font = pygame.font.SysFont("Arial Narrow", 20)
        fontIn = pygame.font.SysFont("Arial Narrow", 30)
        fontBold = pygame.font.SysFont("Arial Narrow", 25)
        fontBold.set_bold(1)
        font = pygame.font.SysFont("Arial Narrow", 25)
        add = self.font.render("Add Node", True, (255, 255, 255))

        # Load images.
        if os.name is "posix":
            buttonUp = pygame.image.load("Imgs/ButtonUp.png")
            buttonDown = pygame.image.load("Imgs/ButtonDown.png")
        else:
            buttonUp = pygame.image.load("Imgs\\ButtonUp.png")
            buttonDown = pygame.image.load("Imgs\\ButtonDown.png")

        # buttons.
        buttonAdd = ButtonP(buttonUp, buttonDown, 100, 650)
        buttonDelete = ButtonP(buttonUp, buttonDown, 200, 650)

        # Loop that allows the pygame window operation.
        while True:
            # With this loop we can get events in the pygame interface.
            for event in pygame.event.get():
                # Here we get the mouse events
                if event.type is pygame.MOUSEBUTTONDOWN:
                    # Here we evaluate if the cursor is on a button.
                    if cursor.colliderect(buttonAdd.rect):
                        self.son = True
                    elif self.son:
                        for connect in self.congress.connections:
                            # Here we evaluate the mouse position for can add and draw new nodes.
                            if (connect.c1.rect.x < pygame.mouse.get_pos()[0] < connect.c1.rect.right 
                                    and connect.c1.rect.y < pygame.mouse.get_pos()[1] < connect.c1.rect.bottom):
                                buttonAdd.add(self.congress, connect.c1, randint(1, 4), 0, json.Read())
                                break
                            elif (connect.c2.rect.x < pygame.mouse.get_pos()[0] < connect.c2.rect.right
                                    and connect.c2.rect.y < pygame.mouse.get_pos()[1] < connect.c2.rect.bottom):
                                buttonAdd.add(self.congress, connect.c2, randint(1, 4), 0, json.Read())
                                break
                        self.son = False
                    elif cursor.colliderect(buttonDelete.rect):
                        buttonDelete.delete(self.congress, randint(1, 30))
                # With this event the output of the initial loop is given.
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((125, 70, 200)) # Window color.
            cursor.update() # update of the cursor position.
            buttonAdd.update(screen, cursor, add) # update of the button image.

            # Drawings on screen.
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 200, 240))
            pygame.draw.rect(screen, (255, 255, 255), (10, 10, 180, 220))
            screen.blit((fontIn.render("INFO", True, (0, 0, 0))), (77, 15))
            screen.blit((fontBold.render("N° Levels:", True, (0, 0, 0))), (15, 50))
            screen.blit((font.render(f"{self.congress.levelMax}", True, (0, 0, 0))), (120, 50))
            screen.blit((fontBold.render("Height:", True, (0, 0, 0))), (15, 75))
            screen.blit((font.render(f"{self.congress.height}", True, (0, 0, 0))), (90, 75))
            screen.blit((fontBold.render("Complete Tree:", True, (0, 0, 0))), (15, 100))
            screen.blit((font.render("", True, (0, 0, 0))), (155, 100))
            screen.blit((fontBold.render("Full Tree:", True, (0, 0, 0))), (15, 125))
            screen.blit((font.render("", True, (0, 0, 0))), (105, 125))
            screen.blit((fontBold.render("Longer way:", True, (0, 0, 0))), (15, 150))
            screen.blit((font.render("", True, (0, 0, 0))), (15, 175))
            self.draw_conect(screen, self.congress.connections)
            self.draw_congress(screen, self.congress.root)
            pygame.display.update()

    # Method that allow draw the nodes.
    def draw_congress(self, screen, parent):
        if parent is None:
            return
        for party in self.congress.parties:
            if parent.party is party.id:
                screen.blit(party.color, (parent.x, parent.y))
                screen.blit((self.font.render(
                    f"  {parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x - 20, parent.y + 30))
        if parent.outside:
            parent.outside = False
            self.outside(parent)
        self.draw_congress(screen, parent.left)
        self.draw_congress(screen, parent.center)
        self.draw_congress(screen, parent.right)

    # Method that allow draw the connections between the nodes.
    def draw_conect(self, screen, connections):
        for conect in connections:
            pygame.draw.line(screen, (0, 0, 0), (conect.c1.x + 12,
                                                 conect.c1.y + 15), (conect.c2.x + 12, conect.c2.y + 15), 10)  

    # Emerging message which is show in case the number of childrens is exceeded.
    def outside(self, parent):
        Tk().withdraw()
        if mb.showinfo("ADVICE", f"The conferee {parent.name} already has the maximum number of political sons, so, it's not possible add more."):
            Tk().destroy()
