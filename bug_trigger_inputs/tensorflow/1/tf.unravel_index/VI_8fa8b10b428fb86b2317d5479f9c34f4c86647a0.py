import pickle
import tensorflow
data = pickle.load(open('8fa8b10b428fb86b2317d5479f9c34f4c86647a0.p', 'rb'))
tensorflow.unravel_index(**data)
