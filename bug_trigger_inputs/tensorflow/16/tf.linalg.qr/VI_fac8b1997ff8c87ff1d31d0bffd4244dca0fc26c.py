import pickle
import tensorflow
data = pickle.load(open('fac8b1997ff8c87ff1d31d0bffd4244dca0fc26c.p', 'rb'))
tensorflow.linalg.qr(**data)
