import pickle
import tensorflow
data = pickle.load(open('f68aec69d701034a39b415689f5f67f1872c8bec.p', 'rb'))
tensorflow.unravel_index(**data)
