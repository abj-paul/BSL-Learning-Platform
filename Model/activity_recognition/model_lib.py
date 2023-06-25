
import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.utils import to_categorical


def get_neural_model(activities):
    log_dir = os.path.join('Logs')
    tb_callback = TensorBoard(log_dir=log_dir)

    model = Sequential()
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(29,1662)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(np.array(activities).shape[0], activation='softmax'))
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    return model, tb_callback

SAMPLE_NUM = 30
FRAME_NUM = 30
def load_activity_data(activities):
    activity_dataset = []
    activity_labels = []
    for activity_index,activity in enumerate(activities):
        for sample_number in range(SAMPLE_NUM):
            single_sample = []
            for frame_number in range(1,FRAME_NUM):
                keypoints = np.load(f'data/{activity}/sample{sample_number}/frame_{frame_number}.npy')
                single_sample.append(keypoints)
            activity_dataset.append(single_sample)
            activity_labels.append(activity_index)
    return np.array(activity_dataset), to_categorical(activity_labels)