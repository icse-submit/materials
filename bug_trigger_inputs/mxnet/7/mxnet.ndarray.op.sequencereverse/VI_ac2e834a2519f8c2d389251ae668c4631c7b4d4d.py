import pickle
import mxnet
data = pickle.load(open('ac2e834a2519f8c2d389251ae668c4631c7b4d4d.p', 'rb'))
mxnet.ndarray.op.SequenceReverse(**data)
