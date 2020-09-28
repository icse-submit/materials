import pickle
import tensorflow
data = pickle.load(open('d53ea972f05a9d55da2ec026bfa783b16918cc8a.p', 'rb'))
tensorflow.nn.conv2d(**data)
