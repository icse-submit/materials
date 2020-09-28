import pickle
import tensorflow
data = pickle.load(open('e3a3778823420c69ce1c05e832816dafeacc8d06.p', 'rb'))
tensorflow.linalg.svd(**data)
