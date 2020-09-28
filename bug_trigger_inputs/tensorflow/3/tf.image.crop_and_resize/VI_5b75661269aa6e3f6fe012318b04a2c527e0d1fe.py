import pickle
import tensorflow
data = pickle.load(open('5b75661269aa6e3f6fe012318b04a2c527e0d1fe.p', 'rb'))
tensorflow.image.crop_and_resize(**data)
