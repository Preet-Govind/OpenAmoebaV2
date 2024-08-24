# create_dummy_model.py

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

def create_dummy_model():
    model = Sequential()
    model.add(Dense(128, input_shape=(5,), activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(2, activation='linear'))
    model.compile(optimizer='adam', loss='mse')
    return model

def generate_dummy_data():
    states = np.random.random((1000, 5))  # Example state data
    actions = np.random.uniform(-1, 1, (1000, 2))  # Example action data
    return states, actions

def train_and_save_model():
    model = create_dummy_model()
    states, actions = generate_dummy_data()
    model.fit(states, actions, epochs=5, batch_size=32)  # Adjust epochs and batch_size as needed
    model.save('amoeba_model.h5')

if __name__ == "__main__":
    train_and_save_model()
