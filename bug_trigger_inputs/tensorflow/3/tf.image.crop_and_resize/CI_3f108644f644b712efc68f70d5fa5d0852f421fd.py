import pickle
import tensorflow
data = pickle.load(open('3f108644f644b712efc68f70d5fa5d0852f421fd.p', 'rb'))
tensorflow.image.crop_and_resize(**data)
