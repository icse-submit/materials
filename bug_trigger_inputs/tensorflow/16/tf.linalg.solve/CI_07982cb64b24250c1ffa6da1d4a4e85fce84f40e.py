import pickle
import tensorflow
data = pickle.load(open('07982cb64b24250c1ffa6da1d4a4e85fce84f40e.p', 'rb'))
tensorflow.linalg.solve(**data)
