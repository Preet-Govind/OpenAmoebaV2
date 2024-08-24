# amoeba.py
import random
import numpy as np
import math
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import pygame

import pygame
import numpy as np

class Amoeba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.model = None

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 15)

    def update(self, food_items, obstacles, toxic_zones):
        state = self.create_state(food_items, obstacles, toxic_zones)
        print(f'state :{state}')
        if self.model:
            action = self.ai_decision(state)
        else:
            action = np.random.choice([0, 1, 2, 3])  # Random action (0: up, 1: down, 2: left, 3: right)

        # Perform the action
        if action == 0:
            self.y -= self.speed  # move up
        elif action == 1:
            self.y += self.speed  # move down
        elif action == 2:
            self.x -= self.speed  # move left
        elif action == 3:
            self.x += self.speed  # move right

        return action

    def ai_decision(self, state):
        if not self.model:
            raise ValueError("Model is not loaded")

        # Predict the action using the AI model
        state = np.array(state).reshape(1, -1)  # Reshape for prediction
        prediction = self.model.predict(state)
        return np.argmax(prediction)

    def create_state(self, food_items, obstacles, toxic_zones):
        # Create a state representation for the AI
        food_positions = [(food.x, food.y) for food in food_items]
        obstacle_positions = [(obstacle.x, obstacle.y) for obstacle in obstacles]
        toxic_zone_positions = [(zone.x, zone.y) for zone in toxic_zones]

        state = {
            'amoeba_position': (self.x, self.y),
            'food_positions': food_positions,
            'obstacle_positions': obstacle_positions,
            'toxic_zone_positions': toxic_zone_positions
        }

        return state
