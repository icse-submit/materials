import pickle
import tensorflow
data = pickle.load(open('c650c0ed47728bc5b83c7ede217b894d2fb43e4c.p', 'rb'))
tensorflow.math.reduce_mean(**data)
