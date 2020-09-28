import pickle
import tensorflow
data = pickle.load(open('c758175568116a7f876a15933fcb3c1745cb1e61.p', 'rb'))
tensorflow.linalg.cholesky_solve(**data)
