import pickle
import tensorflow
data = pickle.load(open('a481b55d254d4ac202b94dfc54debe0fc3b07488.p', 'rb'))
tensorflow.linalg.tridiagonal_matmul(**data)
