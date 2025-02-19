import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv2D, MaxPooling2D, Flatten

import numpy as np

def build_lstm_model():
    model = Sequential()
    # For demonstration, we're using a simple LSTM with an input shape of 10 timesteps and 1 feature.
    model.add(LSTM(50, activation='relu', input_shape=(10, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

# Create a dummy LSTM model instance.
lstm_model = build_lstm_model()
# Optionally load pre-trained weights here.
# lstm_model.load_weights('path/to/lstm_weights.h5')

import numpy as np

def forecast_temperature(data):
    """
    Expects 'data' as a list or array of temperature readings.
    Computes the mean temperature and then applies the formula:
        slowdown = (avg_temp - 65) * 1.7
    """
    data = np.array(data)
    avg_temp = np.mean(data)
    slowdown = (avg_temp - 65) * 1.7
    return slowdown

