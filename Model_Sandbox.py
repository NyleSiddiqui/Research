import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib as plt
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from sklearn.model_selection import train_test_split



if __name__ == '__main__':
	df = pd.read_csv("Subject0.txt", delimiter=';')
	X = df.iloc[:, 0:len(df.columns) - 1]
	y = df.iloc[:, len(df.columns) - 1]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30)
	print(X_train)

	model = keras.Sequential(
		[
			layers.Dense(20, input_dim=4, activation="relu"),
			
			
			
			layers.Dense(35, activation='Softmax')
			
		]
	)
	
