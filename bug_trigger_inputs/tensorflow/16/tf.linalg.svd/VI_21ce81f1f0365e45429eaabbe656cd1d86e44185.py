import pickle
import tensorflow
data = pickle.load(open('21ce81f1f0365e45429eaabbe656cd1d86e44185.p', 'rb'))
tensorflow.linalg.svd(**data)
