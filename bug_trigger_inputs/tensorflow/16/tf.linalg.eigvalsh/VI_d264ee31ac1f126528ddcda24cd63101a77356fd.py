import pickle
import tensorflow
data = pickle.load(open('d264ee31ac1f126528ddcda24cd63101a77356fd.p', 'rb'))
tensorflow.linalg.eigvalsh(**data)
