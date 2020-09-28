import pickle
import mxnet
data = pickle.load(open('34f8989be2fc39bab6e6f0e0a075cda0d38ec53e.p', 'rb'))
mxnet.ndarray.op.SequenceMask(**data)
