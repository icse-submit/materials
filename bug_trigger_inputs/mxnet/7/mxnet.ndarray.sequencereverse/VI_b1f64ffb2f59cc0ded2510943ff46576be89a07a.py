import pickle
import mxnet
data = pickle.load(open('b1f64ffb2f59cc0ded2510943ff46576be89a07a.p', 'rb'))
mxnet.ndarray.SequenceReverse(**data)
