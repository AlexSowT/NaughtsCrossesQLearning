from copy import deepcopy
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split


f = open("data_two_25-01-19-comp2.txt", "r")
dataSet = []
dataList = []
for x in f:
    dataList.append(deepcopy(x))

dataArray = np.asarray(dataList)

for i in range(0,len(dataList)):
    dataList[i] = dataList[i].split("], [[")
    for j in range(0, len(dataList[i])):
        dataList[i][j] = dataList[i][j].replace("[", "")
        dataList[i][j] = dataList[i][j].replace("]", "")
        dataList[i][j] = dataList[i][j].replace("\n", "")
        dataSet.append(deepcopy(dataList[i][j].split(",")))


for i in range(len(dataSet)):
        for j in range(len(dataSet[i])):
            dataSet[i][j] = float(dataSet[i][j])
dataSet = pd.DataFrame(dataSet)
dataSet = dataSet.sample( frac=1)
dataSet = dataSet.drop_duplicates()

X = np.asarray(dataSet.drop(columns=[9]))
y = dataSet[9]
unique_elements, counts_elements = np.unique(y, return_counts=True)

print(np.asarray((unique_elements, counts_elements)))
print(len(y))

y = tf.keras.utils.to_categorical(y)
y = y.reshape(-1,9)


optimi = tf.keras.optimizers.Adam()

model = tf.keras.models.Sequential()

#model = tf.keras.models.load_model("model_25_01_19_first_1.File")

model.add(tf.keras.layers.Dense(9, input_dim=9, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(9, activation='softmax'))



model.compile(optimizer = optimi,
              loss='categorical_crossentropy',
              metrics=['accuracy']
              )

model.fit(X,y, epochs=50)

tf.keras.models.save_model(model, "model_25_01_19_first_comp2.File")







