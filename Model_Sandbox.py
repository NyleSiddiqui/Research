import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'                                                                                
import tensorflow as tf
import pandas as pd
import matplotlib as plt
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from sklearn import preprocessing
from collections import deque
from sklearn.model_selection import train_test_split

SEQ_LEN = 60
TIMESTEP = 3

def preprocess(df):
	df.drop('Subject ID', 1)
	for col in df.columns:                                                                                              #Normalize?
		if  col != "Sex":
			df[col] = df[col].pct_change()
			df.dropna(inplace=True)
			print(col)
			print(np.nan_to_num(df[col].values))
			df[col] = preprocessing.scale(np.nan_to_num(df[col].values))
	df.dropna(inplace=True)
	
	sequential_data = []
	prev_data = deque(maxlen=SEQ_LEN)
	# print(df.head)
	# for c in df.columns:
	# 	print(c)
	


if __name__ == '__main__':
	df = pd.read_csv("master.csv", skiprows=1, names =["Timestamp", "X", "Y", "Button Pressed", "Time", "DistanceX", "DistanceY", "Sex", "Subject ID"])
	df.set_index("Timestamp", inplace=True)
	
	times = sorted(df.index.values)
	last_5pct = times[-int(0.05*len(times))]
	validation = df[(df.index >= last_5pct)]
	df = df[(df.index < last_5pct)]
	
	preprocess(df)
	# train_X, train_y = preprocess(df)
	# validation_X, validation_y = preprocess(df)
	
	#
	# X = df.iloc[:, 0:len(df.columns - 1)].values
	# y = df.iloc[:, len(df.columns) - 1].values
	# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30)
	# print(X_train.shape)
	# X_train = tf.reshape(X_train, (72, 48, 7))
	# y_train = tf.reshape(y_train, (72, 48, 1))
	# print(y_train[0])
	#
	# model = keras.Sequential()
	# model.add(layers.LSTM(128, input_shape=(X_train.shape[1:]), activation='relu', return_sequences=True))
	# model.add(layers.LSTM(128, activation='relu'))
	# model.add(layers.Dense(32, activation='relu'))
	# model.add(layers.Dense(48, activation='softmax'))
	# opt= tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)
	# model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
	# model.fit(X_train, y_train, epochs=2, verbose=1)


