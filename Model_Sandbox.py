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
	test = df.to_numpy()
	X = test[:, 0:len(test[0]) - 1]
	X.reshape(3, 3379, 5)
	y = df.iloc[:, len(test[0]) - 1]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30)

	model = keras.Sequential(
		[
			layers.LSTM(128)
		]
	)

