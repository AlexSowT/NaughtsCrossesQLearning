import tensorflow as tf

data = [[0,2],[1,2],[0,3],[0,2]]

data_onehot = tf.keras.utils.to_categorical(data)

print(data_onehot)