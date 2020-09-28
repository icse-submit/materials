import pickle
import tensorflow
data = pickle.load(open('d9bb42ca5b4d48b8e4c602bbe57157d3b9f7844f.p', 'rb'))
tensorflow.linalg.inv(**data)
