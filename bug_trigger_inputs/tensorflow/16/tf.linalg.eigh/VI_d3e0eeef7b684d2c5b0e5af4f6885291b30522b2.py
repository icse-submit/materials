import pickle
import tensorflow
data = pickle.load(open('d3e0eeef7b684d2c5b0e5af4f6885291b30522b2.p', 'rb'))
tensorflow.linalg.eigh(**data)
