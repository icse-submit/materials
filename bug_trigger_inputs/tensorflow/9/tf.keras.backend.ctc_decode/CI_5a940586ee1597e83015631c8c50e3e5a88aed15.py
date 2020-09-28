import pickle
import tensorflow
data = pickle.load(open('5a940586ee1597e83015631c8c50e3e5a88aed15.p', 'rb'))
tensorflow.keras.backend.ctc_decode(**data)
