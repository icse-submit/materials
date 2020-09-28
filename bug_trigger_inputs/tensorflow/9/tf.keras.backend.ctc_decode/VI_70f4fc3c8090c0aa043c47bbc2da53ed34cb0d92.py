import pickle
import tensorflow
data = pickle.load(open('70f4fc3c8090c0aa043c47bbc2da53ed34cb0d92.p', 'rb'))
tensorflow.keras.backend.ctc_decode(**data)
