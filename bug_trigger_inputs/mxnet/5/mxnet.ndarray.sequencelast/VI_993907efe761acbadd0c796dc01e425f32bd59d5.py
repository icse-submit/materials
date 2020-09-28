import pickle
import mxnet
data = pickle.load(open('993907efe761acbadd0c796dc01e425f32bd59d5.p', 'rb'))
mxnet.ndarray.SequenceLast(**data)
