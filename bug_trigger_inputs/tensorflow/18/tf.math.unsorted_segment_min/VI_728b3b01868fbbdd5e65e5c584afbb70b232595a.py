import pickle
import tensorflow
data = pickle.load(open('728b3b01868fbbdd5e65e5c584afbb70b232595a.p', 'rb'))
tensorflow.math.unsorted_segment_min(**data)
