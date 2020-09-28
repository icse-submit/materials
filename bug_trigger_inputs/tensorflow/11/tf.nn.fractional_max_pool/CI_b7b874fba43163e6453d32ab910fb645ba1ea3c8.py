import pickle
import tensorflow
data = pickle.load(open('b7b874fba43163e6453d32ab910fb645ba1ea3c8.p', 'rb'))
tensorflow.nn.fractional_max_pool(**data)
