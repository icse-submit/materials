import pickle
import tensorflow
data = pickle.load(open('f98df456400a541e514ee028d5d09fd5ae926624.p', 'rb'))
tensorflow.linalg.logm(**data)
