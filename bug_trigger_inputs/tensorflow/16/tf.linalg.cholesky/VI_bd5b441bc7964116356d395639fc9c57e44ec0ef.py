import pickle
import tensorflow
data = pickle.load(open('bd5b441bc7964116356d395639fc9c57e44ec0ef.p', 'rb'))
tensorflow.linalg.cholesky(**data)
