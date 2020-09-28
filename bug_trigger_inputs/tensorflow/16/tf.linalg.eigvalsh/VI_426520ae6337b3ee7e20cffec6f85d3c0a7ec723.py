import pickle
import tensorflow
data = pickle.load(open('426520ae6337b3ee7e20cffec6f85d3c0a7ec723.p', 'rb'))
tensorflow.linalg.eigvalsh(**data)
