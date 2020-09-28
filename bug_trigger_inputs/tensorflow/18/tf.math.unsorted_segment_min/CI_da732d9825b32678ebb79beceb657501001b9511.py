import pickle
import tensorflow
data = pickle.load(open('da732d9825b32678ebb79beceb657501001b9511.p', 'rb'))
tensorflow.math.unsorted_segment_min(**data)
