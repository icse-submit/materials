import pickle
import tensorflow
data = pickle.load(open('3b92873fb4c7c31dc0df1eb4af9dc1ca0fd91912.p', 'rb'))
tensorflow.math.reduce_mean(**data)
