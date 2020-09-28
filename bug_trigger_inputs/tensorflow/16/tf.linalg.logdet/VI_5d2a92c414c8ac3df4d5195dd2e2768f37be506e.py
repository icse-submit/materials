import pickle
import tensorflow
data = pickle.load(open('5d2a92c414c8ac3df4d5195dd2e2768f37be506e.p', 'rb'))
tensorflow.linalg.logdet(**data)
