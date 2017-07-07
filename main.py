import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras.utils.np_utils as kutils

batch_size = 5000
num_classes = 10
epochs = 3

file = pd.read_csv("train.csv").values

# input image dimensions
img_rows, img_cols = 28, 28
input_shape = (img_rows, img_cols, 1)

# Reshaping feature data for 2d Conv. layer
x_train = file[:, 1:].reshape(file.shape[0], img_rows, img_cols, 1)
x_train = x_train.astype(float)
x_train /= 255.0

# Converting output data
y_train = keras.utils.to_categorical(file[:, 0], num_classes)

# Splitting into training & validation data
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.10, random_state=42)

# Building Model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss="categorical_crossentropy",
              optimizer="Adadelta",
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_val, y_val))

score = model.evaluate(x_val, y_val, verbose=0)

print('Test loss:', score[0])