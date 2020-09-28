import pickle
import tensorflow
data = pickle.load(open('756c6baea642e7de648402b691869d396ee67b8a.p', 'rb'))
tensorflow.keras.backend.depthwise_conv2d(**data)
