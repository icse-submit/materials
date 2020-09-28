import pickle
import tensorflow
data = pickle.load(open('df57a1b200cf054e62f6ea92da29e00fb9f5d78f.p', 'rb'))
tensorflow.nn.depth_to_space(**data)
