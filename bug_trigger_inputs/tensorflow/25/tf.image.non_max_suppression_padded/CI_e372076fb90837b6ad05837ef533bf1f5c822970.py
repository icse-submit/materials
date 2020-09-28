import pickle
import tensorflow
data = pickle.load(open('e372076fb90837b6ad05837ef533bf1f5c822970.p', 'rb'))
tensorflow.image.non_max_suppression_padded(**data)
