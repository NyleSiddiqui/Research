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
	df = pd.read_csv("master.csv")
	X = df.iloc[:, 0:len(df.columns) - 1].values
	y = df.iloc[:, len(df.columns) - 1].values
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30)
	X_train = tf.reshape(X_train, (72, 48, 7))
	y_train = tf.reshape(y_train, (72, 48, 1))

	model = keras.Sequential()
	model.add(layers.LSTM(128))
	model.add(layers.Dense(2, input_dim=(72, 128), activation="softmax"))
	model.build((72, 48, 7))
	model.summary()
	model.compile(optimizer='Adam', loss='BinaryCrossentropy')
	model.fit(X_train, y_train, epochs=2)


