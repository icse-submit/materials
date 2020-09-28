import pickle
import tensorflow
data = pickle.load(open('1fe49774445d074a28ac68d707d5c22eb927c33d.p', 'rb'))
tensorflow.linalg.solve(**data)
