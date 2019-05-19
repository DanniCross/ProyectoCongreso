import pygame
import sys
import subprocess
pygame.init()


class GUI:

    def __init__(self, congress):
        self.congress = congress
        self.fuente = None
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
        screen = pygame.display.set_mode(self.screen_size())
        pygame.display.set_caption("Congreso")
        self.fuente = pygame.font.SysFont("Arial Narrow", 20)
        Presi = pygame.image.load("/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/ProyectoI/Imgs/presi.png")
        Red = pygame.image.load("/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/ProyectoI/Imgs/red.png")
        Blue = pygame.image.load("/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/ProyectoI/Imgs/blue.png")
        Yellow = pygame.image.load("/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/ProyectoI/Imgs/yellow.png")
        Green = pygame.image.load("/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/ProyectoI/Imgs/green.png")
        Presi = pygame.transform.scale(Presi, (30, 30))
        Red = pygame.transform.scale(Red, (30, 30))
        Blue = pygame.transform.scale(Blue, (30, 30))
        Yellow = pygame.transform.scale(Yellow, (30, 30))
        Green = pygame.transform.scale(Green, (30, 30))

        while True:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((125, 70, 200))
            self.draw_conect(screen, self.congress.connections)
            self.draw_congress(screen, self.congress.root, Red, Blue, Green, Yellow, Presi)
            pygame.display.update()

    def draw_congress(self, screen, parent, Red, Blue, Green, Yellow, Presi):        
        if parent is None:
            return
        if parent.party == 1:
            screen.blit(Red, (parent.x, parent.y))
            screen.blit((self.fuente.render(f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x, parent.y + 30))
        elif parent.party == 2:
            screen.blit(Blue, (parent.x, parent.y))
            screen.blit((self.fuente.render(f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x, parent.y + 30))
        elif parent.party == 3:
            screen.blit(Green, (parent.x, parent.y))
            screen.blit((self.fuente.render(f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x, parent.y + 30))
        elif parent.party == 4:
            screen.blit(Yellow, (parent.x, parent.y))
            screen.blit((self.fuente.render(f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x, parent.y + 30))
        else:
            screen.blit(Presi, (parent.x, parent.y))
            screen.blit((self.fuente.render(f"{parent.id}.{parent.name}", True, (255, 255, 255))), (parent.x, parent.y + 30))
        if parent.outside:
            alert = pygame.display.set_mode((200, 100))
            pygame.display.set_caption("¡ERROR!")
            message = pygame.font.SysFont("Arial Narrow", 50)
            while True:
                for even in pygame.event.get():
                    if even.type == pygame.QUIT:
                        pygame.quit()
            alert.fill((255, 255, 255))
            alert.blit(self.message.render(f"El congresista {parent.id}.{parent.name} tiene más hijos políticos de los permitidos y no serán agregados."))
            pygame.display.update()
        self.draw_congress(screen, parent.left, Red, Blue, Green, Yellow, Presi)
        self.draw_congress(screen, parent.center, Red, Blue, Green, Yellow, Presi)
        self.draw_congress(screen, parent.right, Red, Blue, Green, Yellow, Presi)
    
    def draw_conect(self, screen, connections):
        for conect in connections:
            pygame.draw.line(screen, (0, 0, 0), (conect.c1.x + 12, conect.c1.y + 15), (conect.c2.x + 12, conect.c2.y + 15), 10)
