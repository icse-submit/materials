import pickle
import tensorflow
data = pickle.load(open('b4954e6394c208eb6df702954f2b9a394c42981b.p', 'rb'))
tensorflow.linalg.slogdet(**data)
