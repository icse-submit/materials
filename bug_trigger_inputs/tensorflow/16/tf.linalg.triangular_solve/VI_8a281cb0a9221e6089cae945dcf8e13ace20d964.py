import pickle
import tensorflow
data = pickle.load(open('8a281cb0a9221e6089cae945dcf8e13ace20d964.p', 'rb'))
tensorflow.linalg.triangular_solve(**data)
