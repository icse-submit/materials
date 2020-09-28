import pickle
import tensorflow
data = pickle.load(open('e719127b25f7851823385d7225345da1d5fc159f.p', 'rb'))
tensorflow.nn.fractional_max_pool(**data)
