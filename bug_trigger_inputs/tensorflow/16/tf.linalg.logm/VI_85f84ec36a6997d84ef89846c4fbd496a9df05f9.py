import pickle
import tensorflow
data = pickle.load(open('85f84ec36a6997d84ef89846c4fbd496a9df05f9.p', 'rb'))
tensorflow.linalg.logm(**data)
