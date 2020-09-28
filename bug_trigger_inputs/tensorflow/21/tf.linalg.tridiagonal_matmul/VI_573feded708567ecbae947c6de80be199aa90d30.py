import pickle
import tensorflow
data = pickle.load(open('573feded708567ecbae947c6de80be199aa90d30.p', 'rb'))
tensorflow.linalg.tridiagonal_matmul(**data)
