import pickle
import tensorflow
data = pickle.load(open('53a96ce1da48b7268c3a980533cbfbda002d8aa0.p', 'rb'))
tensorflow.math.reduce_std(**data)
