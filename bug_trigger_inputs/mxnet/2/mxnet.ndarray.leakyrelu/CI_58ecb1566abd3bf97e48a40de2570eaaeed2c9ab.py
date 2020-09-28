import pickle
import mxnet
data = pickle.load(open('58ecb1566abd3bf97e48a40de2570eaaeed2c9ab.p', 'rb'))
mxnet.ndarray.LeakyReLU(**data)
