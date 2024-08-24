# objects.py
import pygame
import random

class Food:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ToxicZone:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)
