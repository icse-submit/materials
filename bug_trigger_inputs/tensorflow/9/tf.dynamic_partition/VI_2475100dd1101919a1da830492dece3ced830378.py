import pickle
import tensorflow
data = pickle.load(open('2475100dd1101919a1da830492dece3ced830378.p', 'rb'))
tensorflow.dynamic_partition(**data)
