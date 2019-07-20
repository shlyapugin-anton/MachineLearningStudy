import numpy as np
import mnist
import keras

train_images = mnist.train_images()
train_labels = mnist.train_labels()

print(type(train_images))
print(type(train_labels))
