import pygame
import sys
import subprocess
pygame.init()


class GUI:

    def __init__(self):
        self.draw()

    def screen_size(self):
        if self is not 1:
            pass
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
        if self is not 1:
            pass
        screen = pygame.display.set_mode(self.screen_size())
        pygame.display.set_caption("Congreso")

        while True:
            for evento in pygame.event.get():
                if evento.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((255, 255, 255))
            pygame.display.update()
