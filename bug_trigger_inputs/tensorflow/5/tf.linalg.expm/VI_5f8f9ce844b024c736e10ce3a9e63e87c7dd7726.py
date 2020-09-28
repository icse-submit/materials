import pickle
import tensorflow
data = pickle.load(open('5f8f9ce844b024c736e10ce3a9e63e87c7dd7726.p', 'rb'))
tensorflow.linalg.expm(**data)
