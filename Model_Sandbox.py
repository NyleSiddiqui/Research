import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib as plt
# from tensorflow import keras
# from tensorflow.keras import layers, Sequential
from sklearn.model_selection import train_test_split



if __name__ == '__main__':
	df = pd.read_csv("Subject0.csv", delimiter=';', skiprows=1)
	print(df.head())
	X = df.iloc[1:3]
	# y = df.loc[:, 1]
	print("X: {}".format(X))
	# print(y)
	# X_train, X_test, y_train, y_test = train_test_split()
	
