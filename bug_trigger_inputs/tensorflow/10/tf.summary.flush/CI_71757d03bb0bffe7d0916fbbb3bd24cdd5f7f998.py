import pickle
import tensorflow
data = pickle.load(open('71757d03bb0bffe7d0916fbbb3bd24cdd5f7f998.p', 'rb'))
tensorflow.summary.flush(**data)
