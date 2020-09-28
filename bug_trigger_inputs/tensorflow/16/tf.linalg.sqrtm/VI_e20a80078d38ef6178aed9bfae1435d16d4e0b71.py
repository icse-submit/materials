import pickle
import tensorflow
data = pickle.load(open('e20a80078d38ef6178aed9bfae1435d16d4e0b71.p', 'rb'))
tensorflow.linalg.sqrtm(**data)
