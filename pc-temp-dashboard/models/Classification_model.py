import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv2D, MaxPooling2D, Flatten

import numpy as np

def build_cnn_model(input_shape=(64, 64, 1)):
    model = Sequential()
    model.add(Conv2D(32, (3,3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy')
    return model

# Create a dummy CNN model instance.
cnn_model = build_cnn_model()
# Optionally load pre-trained weights here.
# cnn_model.load_weights('path/to/cnn_weights.h5')

def classify_anomaly(image):
    """
    Expects image as a numpy array with shape (64, 64, 1)
    """
    image = np.expand_dims(image, axis=0)  # reshape to (1, 64, 64, 1)
    prediction = cnn_model.predict(image)
    return "anomaly" if prediction[0][0] > 0.5 else "normal"
