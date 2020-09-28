import pickle
import tensorflow
data = pickle.load(open('0d6ca6a141672812f2b9b03e7771d8dae8796e8a.p', 'rb'))
tensorflow.linalg.triangular_solve(**data)
