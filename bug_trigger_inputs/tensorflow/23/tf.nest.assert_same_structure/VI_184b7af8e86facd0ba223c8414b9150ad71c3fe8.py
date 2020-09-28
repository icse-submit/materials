import pickle
import tensorflow
data = pickle.load(open('184b7af8e86facd0ba223c8414b9150ad71c3fe8.p', 'rb'))
tensorflow.nest.assert_same_structure(**data)
