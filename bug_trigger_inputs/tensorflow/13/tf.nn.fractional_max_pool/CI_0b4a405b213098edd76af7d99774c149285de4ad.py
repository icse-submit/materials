import pickle
import tensorflow
data = pickle.load(open('0b4a405b213098edd76af7d99774c149285de4ad.p', 'rb'))
tensorflow.nn.fractional_max_pool(**data)
