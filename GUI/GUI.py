import pygame, sys, os
pygame.init()


class GUI:

    def __init__(self):
        self.dibujar()

    def dibujar(self):
        os.environ['SDL_VIDEO_CENTERED'] = '0'
        ventana = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Congreso")

        while True:
            for evento in pygame.event.get():
                if evento.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            ventana.fill((255, 255, 255))
            pygame.display.update()
