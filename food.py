import pygame

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (0,255,0), (self.x, self.y), 8)
