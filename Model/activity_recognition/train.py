import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split

from model_lib import *


activities = ["gotokal",  "roudro",  "sangbadik"]

X, Y = load_activity_data()



print(X.shape)
print(Y.shape)

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.05)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
model,tb_callback = get_neural_model(activities)
model.summary()
model.fit(x_train, y_train, epochs=200, callbacks=[tb_callback])

model.save("trained_activity_model.h5")
joblib.dump(activities, "labels.joblib")