import pickle
import tensorflow
data = pickle.load(open('bdf3b87269e157dde1662f7f3cea1bc40d93e306.p', 'rb'))
tensorflow.unstack(**data)
