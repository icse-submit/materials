import pickle
import tensorflow
data = pickle.load(open('7db9778032f01552130d19a2a7844cd1608dbfb8.p', 'rb'))
tensorflow.image.resize_with_crop_or_pad(**data)
