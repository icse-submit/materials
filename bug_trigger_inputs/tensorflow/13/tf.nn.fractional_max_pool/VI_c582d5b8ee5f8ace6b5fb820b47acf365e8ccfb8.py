import pickle
import tensorflow
data = pickle.load(open('c582d5b8ee5f8ace6b5fb820b47acf365e8ccfb8.p', 'rb'))
tensorflow.nn.fractional_max_pool(**data)
