import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'                                                                                #Shut the fuck up Tensorflow
import tensorflow as tf
import pandas as pd
import matplotlib as plt
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from sklearn.model_selection import train_test_split





if __name__ == '__main__':
	df = pd.read_csv("master.txt", delimiter=';')
	X = df.iloc[:, 0:len(df.columns) - 1].values
	y = df.iloc[:, len(df.columns) - 1].values
	print(X)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30)
	X_train = tf.reshape(X_train, (15, 473, 5))

	# model = layers.LSTM(128)(X_train)
	# model = layers.Dense(2, activation="softmax")(model)
	# myModel = keras.Model(X_train, model)
	# print(model.summary())


