import pickle
import tensorflow
data = pickle.load(open('0a8b19fa6006ca84755ce25c694d9e6e3603d147.p', 'rb'))
tensorflow.nn.space_to_depth(**data)
