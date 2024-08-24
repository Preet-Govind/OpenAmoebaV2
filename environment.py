import numpy as np
from amoeba import Amoeba
from food import Food
from obstacle import Obstacle
from toxic_zone import ToxicZone
import random
import pygame
from keras.models import load_model

class AmoebaEnvironment:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.food_items = []
        self.obstacles = []
        self.toxic_zones = []
        self.amoeba = Amoeba(self.width // 2, self.height // 2)
        self.data = {
            'states': [],
            'actions': []
        }

        try:
            self.amoeba.model = load_model('amoeba_model.h5')  # Load the pre-trained model if available
        except:
            print("No pre-trained model found. The AI will be random until training is complete.")

    def generate_data(self):
        # Generate food, obstacles, and toxic zones
        self.food_items = [Food(random.randint(0, self.width), random.randint(0, self.height)) for _ in range(5)]
        self.obstacles = [Obstacle(random.randint(0, self.width), random.randint(0, self.height)) for _ in range(5)]
        self.toxic_zones = [ToxicZone(random.randint(0, self.width), random.randint(0, self.height)) for _ in range(5)]

    def update_data(self, state, action):
        # Append the current state and action to the data dictionary
        self.data['states'].append(state)
        self.data['actions'].append(action)

    def draw(self, screen):
        for food in self.food_items:
            food.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for toxic_zone in self.toxic_zones:
            toxic_zone.draw(screen)
        
        # Draw the amoeba
        self.amoeba.draw(screen)

    def train_model(self):
        from keras.models import Sequential
        from keras.layers import Dense
        from keras.optimizers import Adam

        if not self.data['states'] or not self.data['actions']:
            print("No data collected for training.")
            return

        # Convert data to numpy arrays for training
        X_train = np.array([self.flatten_state(state) for state in self.data['states']])
        y_train = np.array(self.data['actions'])

        # Create the model
        model = Sequential()
        model.add(Dense(64, input_shape=(len(X_train[0]),), activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(4, activation='softmax'))  # 4 possible actions (up, down, left, right)

        model.compile(optimizer=Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        
        # Train the model
        model.fit(X_train, y_train, epochs=10, batch_size=32)

        # Save the trained model
        model.save('amoeba_model.h5')
        print("Model training complete and saved as 'amoeba_model.h5'.")

    def flatten_state(self, state):
        # Convert the state dictionary to a flat list of numbers for the neural network
        amoeba_pos = list(state['amoeba_position'])
        food_positions = [coord for pos in state['food_positions'] for coord in pos]
        obstacle_positions = [coord for pos in state['obstacle_positions'] for coord in pos]
        toxic_zone_positions = [coord for pos in state['toxic_zone_positions'] for coord in pos]

        return amoeba_pos + food_positions + obstacle_positions + toxic_zone_positions
