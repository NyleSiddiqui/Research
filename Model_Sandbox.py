import numpy as np
import os
import random
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

import tensorflow as tf
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, BatchNormalization
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from sklearn import preprocessing
from collections import deque

SEQ_LEN = 60
EPOCHS = 10
BATCH_SIZE = 60
NAME = f"SEQ-{SEQ_LEN}-{int(time.time())}"

def preprocess(df):
	# df = df.values
	# norm = df[:-1]
	# print(norm[0:2])
	# min_max_scalar = preprocessing.MinMaxScaler()
	# df = min_max_scalar.fit_transform(df)
	for col in df.columns:
		if col != "Subject ID":
			df[col] = preprocessing.normalize([i[:-1] for i in df.values], axis=1)
	
	df = df.values
	sequential_data = []
	prev_data = deque(maxlen=SEQ_LEN)
	# targets = np.empty(SEQ_LEN)
	for i in df:
		# count = 0
		# for j in i:
		# 	count += 1
		# 	if count == 8:
		# 		targets.
		# if targets.
		prev_data.append([n for n in i[:-1]])
		if len(prev_data) == SEQ_LEN:
			sequential_data.append([np.array(prev_data), i[-1]])
	random.shuffle(sequential_data)
	X = []
	y = []
	for seq, target in sequential_data:
		X.append(seq)
		y.append(target)
	return np.array(X), np.array(y)
	





if __name__ == '__main__':
	pd.set_option('display.max_columns', None)
	pd.set_option('display.width', None)
	df = pd.read_csv("22master.csv", skiprows=1, names =["Timestamp", "X", "Y", "Button Pressed", "Time", "DistanceX", "DistanceY", "Speed", "Acceleration", "Sex", "Subject ID"])
	df.set_index("Timestamp", inplace=True)
	
	times = sorted(df.index.values)
	split = times[-int(0.1*len(times))]
	validation = df[(df.index >= split)]
	df = df[(df.index < split)]
	train_X, train_y = preprocess(df)
	validation_X, validation_y = preprocess(validation)


	model = Sequential()
	model.add(LSTM(256, input_shape=(train_X.shape[1:]), return_sequences=True))#, activation='tanh', recurrent_activation='sigmoid', recurrent_dropout=0,  unroll=False, use_bias=True))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())

	model.add(LSTM(128, input_shape=(train_X.shape[1:]), return_sequences=True))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())
	
	model.add(LSTM(128, input_shape=(train_X.shape[1:]), return_sequences=True))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())
	
	model.add(LSTM(128, input_shape=(train_X.shape[1:]), return_sequences=True))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())
	
	model.add(LSTM(128, input_shape=(train_X.shape[1:]), return_sequences=True))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())
	
	model.add(LSTM(128, input_shape=(train_X.shape[1:]), return_sequences=True))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())

	model.add(LSTM(128, input_shape=(train_X.shape[1:])))
	model.add(Dropout(0.2))
	model.add(BatchNormalization())

	model.add(Dense(64, activation='relu'))
	model.add(Dropout(0.2))
	
	model.add(Dense(32, activation='relu'))
	model.add(Dropout(0.2))

	model.add(Dense(4, activation='softmax'))

	opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-6)

	model.compile(loss='sparse_categorical_crossentropy',
	              optimizer=opt,
	              metrics=['accuracy'])
	# tensorboard = TensorBoard(log_dir=f'logs/{NAME}')

	filepath = "RNN_Final-{epoch:02d}-{{val_acc:.3f}"
	# checkpoint = ModelCheckpoint("models/{}.model".format(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max'))


	model.summary()
	history = model.fit(train_X, train_y,
	                    epochs=EPOCHS,
	                    batch_size=BATCH_SIZE,
	                    validation_data=(validation_X, validation_y),
	                    # callbacks=[tensorboard, checkpoint],
	                    verbose=1)


