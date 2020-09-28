import pickle
import tensorflow
data = pickle.load(open('c476567112bba19d132a3794b860d8ce1c08d6a4.p', 'rb'))
tensorflow.linalg.logdet(**data)
