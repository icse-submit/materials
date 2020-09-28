import pickle
import tensorflow
data = pickle.load(open('06965284b47d9e07a0da74ce66be42e369a8620f.p', 'rb'))
tensorflow.linalg.eigh(**data)
