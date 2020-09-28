import pickle
import tensorflow
data = pickle.load(open('a066146fced6993899136f812af765466a12164b.p', 'rb'))
tensorflow.linalg.inv(**data)
