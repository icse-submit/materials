import pickle
import tensorflow
data = pickle.load(open('f2a1e8d368b7dec188a152818fa28de1830ae896.p', 'rb'))
tensorflow.nn.conv2d(**data)
