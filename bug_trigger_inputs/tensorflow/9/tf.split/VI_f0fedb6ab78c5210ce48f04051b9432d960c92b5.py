import pickle
import tensorflow
data = pickle.load(open('f0fedb6ab78c5210ce48f04051b9432d960c92b5.p', 'rb'))
tensorflow.split(**data)
