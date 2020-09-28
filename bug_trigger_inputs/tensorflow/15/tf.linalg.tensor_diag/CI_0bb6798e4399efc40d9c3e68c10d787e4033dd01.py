import pickle
import tensorflow
data = pickle.load(open('0bb6798e4399efc40d9c3e68c10d787e4033dd01.p', 'rb'))
tensorflow.linalg.tensor_diag(**data)
