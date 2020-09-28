import pickle
import tensorflow
data = pickle.load(open('9fe0c765ee8b1fe88ac7f98a4fdf7b8bc3bad20a.p', 'rb'))
tensorflow.math.reduce_variance(**data)
