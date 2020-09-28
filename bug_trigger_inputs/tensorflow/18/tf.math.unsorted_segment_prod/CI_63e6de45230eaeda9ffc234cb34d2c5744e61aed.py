import pickle
import tensorflow
data = pickle.load(open('63e6de45230eaeda9ffc234cb34d2c5744e61aed.p', 'rb'))
tensorflow.math.unsorted_segment_prod(**data)
