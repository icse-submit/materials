import pickle
import tensorflow
data = pickle.load(open('5d23b3b33853b471081cf5f4d6f46d7a8c210012.p', 'rb'))
tensorflow.math.reduce_std(**data)
