import pygame

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 20, 20))
