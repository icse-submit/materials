import pickle
import tensorflow
data = pickle.load(open('0e79ce328115034b6e84485c62ad013d7da61ef1.p', 'rb'))
tensorflow.math.reduce_mean(**data)
