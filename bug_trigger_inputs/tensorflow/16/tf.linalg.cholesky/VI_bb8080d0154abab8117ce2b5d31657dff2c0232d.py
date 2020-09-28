import pickle
import tensorflow
data = pickle.load(open('bb8080d0154abab8117ce2b5d31657dff2c0232d.p', 'rb'))
tensorflow.linalg.cholesky(**data)
