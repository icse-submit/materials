import pickle
import mxnet
data = pickle.load(open('ff07b8a32e899140e7774017dea917b442461bae.p', 'rb'))
mxnet.ndarray.op.SequenceReverse(**data)
