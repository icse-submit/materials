import pickle
import tensorflow
data = pickle.load(open('5e47bde94de756f583e306b5f42c60ea855112b0.p', 'rb'))
tensorflow.math.unsorted_segment_sum(**data)
