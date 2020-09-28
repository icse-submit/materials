import pickle
import mxnet
data = pickle.load(open('3156e184c754ae7afbc14686d17c398a6b4179a7.p', 'rb'))
mxnet.ndarray.SequenceReverse(**data)
