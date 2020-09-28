import pickle
import tensorflow
data = pickle.load(open('a6485ed0a5c4465279990fedaefc1b47422cdb97.p', 'rb'))
tensorflow.unstack(**data)
