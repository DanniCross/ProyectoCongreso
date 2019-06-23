import pygame
import subprocess
import os
import ctypes
from tkinter import *
from tkinter import messagebox as mb
from tkinter import font as f
from Views.cursor import Cursor
from Views.button import ButtonP
from random import randint
from Json.JSONN import JSON2
pygame.init()  # Pygame initialization.


# Graphical user interface class.
class GUI:

    def __init__(self, congress):
        # Entry of the congress class to the GUI init.
        self.congress = congress
        self.font = None
        self.son = False
        self.delete = False
        self.change = False
        self.Full = "No"
        self.Complete = "No"
        # Called to the Cursor class for recognize the mouse with pygame.
        self.cursor = Cursor()
        self.draw()  # Called to the draw method where is the GUI code.
        self.slash = ""

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
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        size = (ancho, alto)
        return size

    def draw(self):
        json = JSON2()
        cursor = Cursor()
        if os.name is "posix":
            # Window size defnition.
            screen = pygame.display.set_mode(self.screen_size())
            self.slash = "/"
        else:
            screen = pygame.display.set_mode(
                self.screen_sizeW(), pygame.RESIZABLE)
            self.slash = "\\"
        pygame.display.set_caption("Congress")

        # fonts.
        self.font = pygame.font.SysFont("Times New Roman", 11)
        fontIn = pygame.font.SysFont("Times New Roman", 25)
        fontBold = pygame.font.SysFont("Times New Roman", 16)
        fontBold.set_bold(1)
        font = pygame.font.SysFont("Times New Roman", 16)
        verify = self.font.render("Verify assistance.", True, (255, 255, 255))
        add = self.font.render("Enter new conferee.", True, (255, 255, 255))
        delete = self.font.render("Suspend conferee.", True, (255, 255, 255))
        change = self.font.render("Replace conferee", True, (255, 255, 255))

        # Load images.
        buttonUp = pygame.image.load(f"Imgs{self.slash}ButtonUp.png")
        buttonDown = pygame.image.load(f"Imgs{self.slash}ButtonDown.png")

        # buttons.
        buttonAdd = ButtonP(pygame.transform.scale(buttonUp, (140, 30)),
                            pygame.transform.scale(buttonDown, (140, 30)), 100, 650)
        buttonDelete = ButtonP(pygame.transform.scale(buttonUp, (140, 30)),
                               pygame.transform.scale(buttonDown, (140, 30)), 420, 650)
        BtnPresence = ButtonP(pygame.transform.scale(buttonUp, (130, 30)),
                              pygame.transform.scale(buttonDown, (130, 30)), 260, 650)
        BtnChange = ButtonP(pygame.transform.scale(buttonUp, (140, 30)),
                            pygame.transform.scale(buttonDown, (140, 30)), 580, 650)

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
                                buttonAdd.add(self.congress, connect.c1, randint(
                                    1, 4), 0, json.Read())
                                break
                            elif (connect.c2.rect.x < pygame.mouse.get_pos()[0] < connect.c2.rect.right
                                    and connect.c2.rect.y < pygame.mouse.get_pos()[1] < connect.c2.rect.bottom):
                                buttonAdd.add(self.congress, connect.c2, randint(
                                    1, 4), 0, json.Read())
                                break
                        self.son = False
                    elif cursor.colliderect(buttonDelete.rect):
                        self.delete = True
                    elif self.delete:
                        for connect in self.congress.connections:
                            # Here we evaluate the mouse position for can add and delete nodes
                            if (connect.c1.rect.x < pygame.mouse.get_pos()[0] < connect.c1.rect.right
                                    and connect.c1.rect.y < pygame.mouse.get_pos()[1] < connect.c1.rect.bottom):
                                self.congress = buttonDelete.delete(self.congress, connect.c1)
                                break
                            elif (connect.c2.rect.x < pygame.mouse.get_pos()[0] < connect.c2.rect.right
                                    and connect.c2.rect.y < pygame.mouse.get_pos()[1] < connect.c2.rect.bottom):
                                self.congress = buttonDelete.delete(self.congress, connect.c2)
                                break
                        self.delete = False

                    elif cursor.colliderect(BtnPresence.rect):
                        screenTK = Tk()
                        size = self.screen_size()
                        screenTK.geometry(
                            f"430x110+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK.title("Verify assitance")
                        tour = IntVar()
                        time = IntVar(value=1)
                        textT = StringVar(
                            value="Choose the time between one call and another.")
                        textB = StringVar(
                            value="Choose the way to check assitance.")
                        labelTime = Label(
                            screenTK, textvariable=textT).place(x=5, y=5)
                        time_field = Spinbox(screenTK, from_=1, to=10,
                                             wrap=True, textvariable=time).place(x=5, y=25, width=35)
                        labelTours = Label(
                            screenTK, textvariable=textB).place(x=5, y=50)
                        Button(screenTK, text="Width tour",
                               command=lambda: self.tour(screenTK, tour, 1)).place(x=5, y=70)
                        Button(screenTK, text="Preorder tour",
                               command=lambda: self.tour(screenTK, tour, 2)).place(x=100, y=70)
                        Button(screenTK, text="Inorder tour",
                               command=lambda: self.tour(screenTK, tour, 3)).place(x=213, y=70)
                        Button(screenTK, text="Posorder tour",
                               command=lambda: self.tour(screenTK, tour, 4)).place(x=320, y=70)
                        screenTK.mainloop()
                        BtnPresence.verify_assitance(
                            screen, self.congress, time.get(), tour.get())
                    
                    elif cursor.colliderect(BtnChange.rect):
                        self.change = True

                    elif self.change:
                        temp = None
                        for connect in self.congress.connections:
                            # Here we evaluate the mouse position for can add and delete nodes
                            if (connect.c1.rect.x < pygame.mouse.get_pos()[0] < connect.c1.rect.right
                                    and connect.c1.rect.y < pygame.mouse.get_pos()[1] < connect.c1.rect.bottom):
                                temp = connect.c1
                                break
                            elif (connect.c2.rect.x < pygame.mouse.get_pos()[0] < connect.c2.rect.right
                                    and connect.c2.rect.y < pygame.mouse.get_pos()[1] < connect.c2.rect.bottom):
                                temp = connect.c2
                                break
                        screenTK2 = Tk()
                        size = self.screen_size()
                        screenTK2.geometry(
                            f"250x150+{int(size[0]/2) - 130}+{int(size[1]/2) - 100}")
                        screenTK2.title("Replace Conferee")
                        id = IntVar()
                        name = StringVar()
                        textName = StringVar(
                            value="Write suplent's name.")
                        textId = StringVar(
                            value="Write suplent's id.")
                        labelId = Label(
                            screenTK2, textvariable=textId).place(x=10, y=5)
                        labelName = Label(
                            screenTK2, textvariable=textName).place(x=10, y=50)
                        id_field = Spinbox(screenTK2, from_=(self.congress.max + 1), to=100, wrap=True, textvariable = id, width=37).place(x = 10, y = 25)
                        name_field = Entry(screenTK2, textvariable = name, width=37).place(x = 10, y = 70)
                        Button(screenTK2, text="Change", command=lambda: self.send(
                            screenTK2), height=3).place(x=95, y=95)
                        screenTK2.mainloop()
                        self.congress.root = BtnChange.change(self.congress, temp, id.get(), name.get())
                        self.change = False

                # With this event the output of the initial loop is given.
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((125, 70, 200))  # Window color.
            cursor.update()  # update of the cursor position.
            # update of the button image.
            buttonAdd.update(screen, cursor, add)
            BtnPresence.update(screen, cursor, verify)
            buttonDelete.update(screen, cursor, delete)
            BtnChange.update(screen, cursor, change)

            # Drawings on screen.
            if self.congress.Full:
                self.Full = "Yes"
                self.Complete = "Yes"
            elif self.congress.Complete:
                self.Complete = "Yes"
                self.Full = "No"
            else:
                self.Complete = "No"
                self.Full = "No"
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 200, 240))
            pygame.draw.rect(screen, (255, 255, 255), (10, 10, 180, 220))
            screen.blit((fontIn.render("INFO", True, (0, 0, 0))), (77, 15))
            screen.blit(
                (fontBold.render("N° Levels:", True, (0, 0, 0))), (15, 50))
            screen.blit(
                (font.render(f"{self.congress.levelMax}", True, (0, 0, 0))), (120, 50))
            screen.blit(
                (fontBold.render("Height:", True, (0, 0, 0))), (15, 75))
            screen.blit(
                (font.render(f"{self.congress.height}", True, (0, 0, 0))), (90, 75))
            screen.blit(
                (fontBold.render("Complete Tree:", True, (0, 0, 0))), (15, 100))
            screen.blit(
                (font.render(f"{self.Complete}", True, (0, 0, 0))), (155, 100))
            screen.blit(
                (fontBold.render("Full Tree:", True, (0, 0, 0))), (15, 125))
            screen.blit(
                (font.render(f"{self.Full}", True, (0, 0, 0))), (105, 125))
            screen.blit(
                (fontBold.render("Longer way:", True, (0, 0, 0))), (15, 150))
            screen.blit(
                (font.render(f"{self.congress.way}", True, (0, 0, 0))), (15, 175))
            self.draw_conect(screen, self.congress.connections)
            self.draw_congress(screen, self.congress.root)
            pygame.display.update()

    # Method that allow draw the nodes.
    def draw_congress(self, screen, parent):
        if parent is None:
            return
        for party in self.congress.parties:
            if parent.id is party.leader:
                pygame.draw.circle(screen, (205, 164, 52),
                                   (parent.x + 15, parent.y), 10, 10)
            if parent.party is party.id:
                screen.blit(party.color, (parent.x, parent.y))
                screen.blit((self.font.render(
                    f"  {parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x - 30, parent.y + 30))
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

    def tour(self, screen, tour, method):
        tour.set(method)
        screen.destroy()
    
    def send(self, screen):
        screen.destroy()
