import pygame
import sys
from Views.button import Button
from Views.cursor import Cursor

pygame.init()


class OUTSIDE:
    
    def outside(self, conferee):
        screen = pygame.display.set_mode((200, 200), pygame.NOFRAME)
        pygame.display.caption("ADVICE")
        cursor = Cursor()
        buttonUp = pygame.image.load("Imgs/ButtonUp.png")
        buttonDown = pygame.image.load("Imgs/ButtonDown.png")
        OK = Button(buttonUp, buttonDown, 100, 180)

        while True:
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    if cursor.colliderect(OK.rect):
                        pygame.quit()
                        sys.exit()
