import pickle
import tensorflow
data = pickle.load(open('66b12cc09b5f0272846d033e045b2e116cd15a9d.p', 'rb'))
tensorflow.signal.overlap_and_add(**data)
