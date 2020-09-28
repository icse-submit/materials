import pickle
import tensorflow
data = pickle.load(open('70fb5bee3d81865ad8cf0251d724d02fcf1e56e1.p', 'rb'))
tensorflow.math.unsorted_segment_prod(**data)
