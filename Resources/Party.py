import pygame

# Class that allows create each of the 4 political parties how an object.
class Party:

    def __init__(self, id, name, leader, color):
        self.id = id
        self.name = name
        self.leader = leader
        self.color = pygame.transform.scale(pygame.image.load(color), (30, 30))
