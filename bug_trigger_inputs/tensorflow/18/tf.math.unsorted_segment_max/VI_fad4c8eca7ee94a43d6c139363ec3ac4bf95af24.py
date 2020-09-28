import pickle
import tensorflow
data = pickle.load(open('fad4c8eca7ee94a43d6c139363ec3ac4bf95af24.p', 'rb'))
tensorflow.math.unsorted_segment_max(**data)
