import pickle
import tensorflow
data = pickle.load(open('7d52b117448e90ad7577270acd53d527ec0dfb2b.p', 'rb'))
tensorflow.math.reduce_mean(**data)
