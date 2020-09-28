import pickle
import tensorflow
data = pickle.load(open('da401102faa9762d739538daf0fc1954ecc8099e.p', 'rb'))
tensorflow.linalg.svd(**data)
