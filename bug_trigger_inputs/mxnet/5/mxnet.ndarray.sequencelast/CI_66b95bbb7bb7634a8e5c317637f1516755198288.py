import pickle
import mxnet
data = pickle.load(open('66b95bbb7bb7634a8e5c317637f1516755198288.p', 'rb'))
mxnet.ndarray.SequenceLast(**data)
