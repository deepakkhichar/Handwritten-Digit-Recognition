# -*- coding: utf-8 -*-
"""cifar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JGfMAWvGOENNjf9BmVrREqCPHK3eXfjh
"""

import tensorflow as tf
from tensorflow.keras import  datasets , layers , models
import matplotlib.pyplot as plt
import numpy as np

"""**Downloading  Dataset.**"""

(X_train , y_train), (X_test, y_test) = datasets.cifar10.load_data()
X_train.shape

print('Training Images: {}'.format(X_train.shape))
print('Testing Images: {}'.format(X_train.shape))

print(X_train[0].shape)

y_train = y_train.reshape(-1,)
y_train[:5]

"""**Declaration of Classes**"""

classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

"""**Normalizing the dataset**"""

seed = 6
np.random.seed(seed)


X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train = X_train / 255
X_test = X_test / 255

"""**Validating Normalised dataset**"""

print(X_train[0])

"""**Model building**"""

import tensorflow as tf

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense, Conv2D , MaxPool2D , Dropout

"""**Initial Model**"""

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3,3), padding='same',activation = 'relu', input_shape=[32,32,3]))


model.add(Conv2D(filters=64, kernel_size=(3,3), padding='same',activation = 'relu'))
model.add(MaxPool2D(pool_size=(2,2),padding = 'valid'))
model.add(Dropout(0.5))

model.add(Conv2D(filters=128, kernel_size=(5,5), padding='same',activation = 'relu'))
model.add(MaxPool2D(pool_size=(4,4),padding = 'valid'))
model.add(Dropout(0.5))


model.add(Flatten())
model.add(Dense(units = 128, activation ='relu'))
model.add(Dense(units=10, activation = 'softmax'))

model.summary()

"""**Comparing Training accuracy with Validation Accuracy**"""

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics= ['sparse_categorical_accuracy'])

history = model.fit(X_train, y_train, batch_size=10, epochs=10, verbose=1, validation_data=(X_test, y_test))

"""**Graphical representation**"""

epoch_range = range(1, 11)
plt.plot(epoch_range, history.history['sparse_categorical_accuracy'])
plt.plot(epoch_range, history.history['val_sparse_categorical_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Val'], loc='upper left')
plt.show()

plt.plot(epoch_range, history.history['loss'])
plt.plot(epoch_range, history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('loss')
plt.xlabel('Epoch')
plt.legend(['Train','val'], loc='upper left')
plt.show()

"""**Final Model**"""

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3,3), padding='same',activation = 'relu', input_shape=[32,32,3]))


model.add(Conv2D(filters=64, kernel_size=(3,3), padding='same',activation = 'relu'))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2),padding = 'valid'))


model.add(Conv2D(filters=128, kernel_size=(5,5), padding='same',activation = 'relu'))
model.add(MaxPool2D(pool_size=(4,4),strides=(2,2),padding = 'valid'))


model.add(Conv2D(filters=128, kernel_size=(5,5), padding='same',activation = 'relu'))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2),padding = 'valid'))


model.add(Dropout(0.2))


model.add(Flatten())
model.add(Dense(units = 128, activation ='relu'))
model.add(Dense(units=10, activation = 'softmax'))

model.summary()

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics= ['sparse_categorical_accuracy'])

"""**Testing Accuracy of the model**"""

history = model.fit(X_train, y_train, batch_size=10, epochs=15, verbose=1, validation_data=(X_test, y_test))

"""**Graphical Representation**"""

epoch_range = range(1, 11)
plt.plot(epoch_range, history.history['sparse_categorical_accuracy'])
plt.plot(epoch_range, history.history['val_sparse_categorical_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Val'], loc='upper left')
plt.show()

plt.plot(epoch_range, history.history['loss'])
plt.plot(epoch_range, history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('loss')
plt.xlabel('Epoch')
plt.legend(['Train','val'], loc='upper left')
plt.show()