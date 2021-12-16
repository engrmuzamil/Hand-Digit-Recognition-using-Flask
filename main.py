from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model


img = cv2.imread('digit.png')
save_model = tf.keras.models.load_model('new_model.h5')

gray = img[:,:,0]
gray = cv2.resize(gray, (28,28))
gray = gray/ 255
new = gray.reshape(1,28*28,)
predict = save_model.predict(new)
predict = predict.argmax()
print(predict)

