import pickle
import tensorflow
data = pickle.load(open('0a7c0749c87a64abe9a6ed70a59c3839eef1a21a.p', 'rb'))
tensorflow.dynamic_partition(**data)
