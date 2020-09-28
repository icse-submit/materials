import pickle
import tensorflow
data = pickle.load(open('8ad85d9f7344f2b81ea8128462e44e809f07b4cd.p', 'rb'))
tensorflow.math.unsorted_segment_sum(**data)
