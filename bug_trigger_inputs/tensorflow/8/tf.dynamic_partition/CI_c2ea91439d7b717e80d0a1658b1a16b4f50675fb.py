import pickle
import tensorflow
data = pickle.load(open('c2ea91439d7b717e80d0a1658b1a16b4f50675fb.p', 'rb'))
tensorflow.dynamic_partition(**data)
