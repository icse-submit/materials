import pickle
import tensorflow
data = pickle.load(open('7f07dfb3e0c5eea03d2bbfbf1d1f96c0edad78f4.p', 'rb'))
tensorflow.image.combined_non_max_suppression(**data)
