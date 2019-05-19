import pygame
import sys
import subprocess
pygame.init()


class GUI:

    def __init__(self, root):
        self.root = root
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
        Presi = pygame.image.load(
            "/home/camilog/Descargas/ProyectosVscode/ProyectoCongresoED2/Imgs/Presi.png")
        Red = pygame.image.load(
            "/home/camilog/Descargas/ProyectosVscode/ProyectoCongresoED2/Imgs/Rojo.png")
        Blue = pygame.image.load(
            "/home/camilog/Descargas/ProyectosVscode/ProyectoCongresoED2/Imgs/Azul.png")
        Yellow = pygame.image.load(
            "/home/camilog/Descargas/ProyectosVscode/ProyectoCongresoED2/Imgs/Amarillo.png")
        Green = pygame.image.load(
            "/home/camilog/Descargas/ProyectosVscode/ProyectoCongresoED2/Imgs/Verde.png")

        green = (0, 255, 0)
        red = (255, 0, 0)
        blue = (0, 0, 255)
        yellow = (255, 255, 000)
        posPresident = (680, 50)
        radius = 20
        width = 2

        while True:
            for evento in pygame.event.get():
                if evento.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((255, 255, 255))
            screen.blit(Presi, (680,70) )
            pygame.display.update()
