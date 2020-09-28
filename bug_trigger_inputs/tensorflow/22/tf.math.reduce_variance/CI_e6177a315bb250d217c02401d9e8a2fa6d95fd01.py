import pickle
import tensorflow
data = pickle.load(open('e6177a315bb250d217c02401d9e8a2fa6d95fd01.p', 'rb'))
tensorflow.math.reduce_variance(**data)
