import pickle
import tensorflow
data = pickle.load(open('53c877664b9474903617fe29081df40618a1717a.p', 'rb'))
tensorflow.nn.depth_to_space(**data)
