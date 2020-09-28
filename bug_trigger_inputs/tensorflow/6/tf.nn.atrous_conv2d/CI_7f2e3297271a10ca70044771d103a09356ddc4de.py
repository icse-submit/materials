import pickle
import tensorflow
data = pickle.load(open('7f2e3297271a10ca70044771d103a09356ddc4de.p', 'rb'))
tensorflow.nn.atrous_conv2d(**data)
