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

from sklearn.metrics import accuracy_score
from collections import deque

SEQ_LEN = 100
EPOCHS = 25
BATCH_SIZE = 250
NAME = f"SEQ-{SEQ_LEN}-{int(time.time())}" #For saving model, not in use

def preprocess(df):
	df.rename(columns={"Speed": "X_Speed", "Acceleration": "X_Acceleration"}, inplace=True)
	df.insert(len(df.columns) - 1, "Y_Speed", 0)
	df.insert(len(df.columns) - 1, "Y_Acceleration", 0)
	df.insert(len(df.columns) - 1, "Speed", 0)
	df.insert(len(df.columns) - 1, "Acceleration", 0)
	df.insert(len(df.columns) - 1, "Jerk", 0)
	df.insert(len(df.columns) - 1, "Ang_V", 0)
	df.insert(len(df.columns) - 1, "Path_Tangent", 0)
	del df['Sex'] # No need for gender feature anymore
	df = df.loc[(df["X"].shift() != df["X"]) | (df["Y"].shift() != df["Y"])]
	print(df.head())
	df['X_Speed'] = (df.X - df.X.shift(1)) / (df.Timestamp - df.Timestamp.shift(1))
	df['Y_Speed'] = (df.Y - df.Y.shift(1)) / (df.Timestamp - df.Timestamp.shift(1))
	df['Speed'] = np.sqrt((df.X_Speed**2) + (df.Y_Speed**2))
	df['X_Acceleration'] =  (df.X_Speed - df.X_Speed.shift(1)) / (df.Timestamp - df.Timestamp.shift(1))
	df['Y_Acceleration'] = (df.Y_Speed - df.Y_Speed.shift(1)) / (df.Timestamp - df.Timestamp.shift(1))
	df['Acceleration'] = (df.Speed - df.Speed.shift(1)) / (df.Timestamp - df.Timestamp.shift(1))
	df['Jerk'] = (df.Acceleration - df.Acceleration.shift(1)) / (df.Timestamp - df.Timestamp.shift(1))
	df['Path_Tangent'] = np.arctan2((df.Y - df.Y.shift(1)), (df.X - df.X.shift(1)))
	df['Ang_V'] = (df.Path_Tangent - df.Path_Tangent.shift(1)) / (df.Timestamp - df.Timestamp.shift(1))
	df = df.fillna(0)
	print(df.head())

	for col in df.columns:
		if col not in ["Subject ID"]:
			df[col] = preprocessing.normalize([i[:-1] for i in df.values], axis=1) #normalize each feature separately. TODO: Subject to change - default norm is 'l1' norm,  use 'max' norm? Also maybe change axis to 0? https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html
			
	df = df.values
	sequential_data = []
	prev_data = deque(maxlen=SEQ_LEN)
	for i in df:
		prev_data.append([n for n in i[1:-1]]) # Append each row in df to prev_data without 'Subject ID' column, up to 60 rows
		if len(prev_data) == SEQ_LEN:
			sequential_data.append([np.array(prev_data), i[-1]]) # Prev_data now contains SEQ_LEN (60) amount of samples and can be appended as one batch of 60 for RNN
	random.shuffle(sequential_data)
	X = []
	y = []
	for seq, target in sequential_data:
		X.append(seq)
		y.append(target)
	X = np.array(X)
	y = np.array(y)
	return X, y
	

if __name__ == '__main__':
	# np.set_printoptions(threshold=np.inf)
	pd.options.mode.chained_assignment = None
	pd.set_option('display.max_columns', None)
	pd.set_option('display.width', None)
	train_df = pd.read_csv("Research Code/Collected/Subject0val.csv", skiprows=1, names =["Timestamp", "X", "Y", "Button Pressed", "Time", "DistanceX", "DistanceY", "Speed", "Acceleration", "Sex", "Subject ID"])
	val_df = pd.read_csv("Research Code/Collected/Subject0val.csv", skiprows=1, names =["Timestamp", "X", "Y", "Button Pressed", "Time", "DistanceX", "DistanceY", "Speed", "Acceleration", "Sex", "Subject ID"])
	test_df = pd.read_csv("Research Code/Collected/Subject0test.csv", skiprows=1, names =["Timestamp", "X", "Y", "Button Pressed", "Time", "DistanceX", "DistanceY", "Speed", "Acceleration", "Sex", "Subject ID"])
	train_df.set_index("Timestamp", inplace=False)
	val_df.set_index("Timestamp", inplace=False)
	test_df.set_index("Timestamp", inplace=False)
	train_X, train_y = preprocess(train_df)
	print("Done with train")
	validation_X, validation_y = preprocess(val_df)
	print("Done with val")
	test_X, test_y = preprocess(test_df)
	print("Done with test")
	model = Sequential()
	
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
	
	model.add(Dense(40, activation='softmax'))

	opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-6)

	model.compile(loss='sparse_categorical_crossentropy',
	              optimizer=opt,
	              metrics=['accuracy'])
	#tensorboard = TensorBoard(log_dir=f'logs/{NAME}')

	#filepath = "RNN_Final-{epoch:02d}-{{val_acc:.3f}"
	# checkpoint = ModelCheckpoint("models/{}.model".format(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max'))
	model.summary()
	history = model.fit(train_X, train_y,
	                    epochs=EPOCHS,
	                    batch_size=BATCH_SIZE,
	                    validation_data=(validation_X, validation_y),
	                    #callbacks=[tensorboard, checkpoint],
	                    verbose=1)
	history
	model.save('saved_model-real-25.h5')
	model.save_weights('saved_model-real-25weights.h5')
	results = model.evaluate(test_X, test_y, verbose=1)
	results

