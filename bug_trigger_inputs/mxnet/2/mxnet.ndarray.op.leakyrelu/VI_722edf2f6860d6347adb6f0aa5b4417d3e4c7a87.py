import pickle
import mxnet
data = pickle.load(open('722edf2f6860d6347adb6f0aa5b4417d3e4c7a87.p', 'rb'))
mxnet.ndarray.op.LeakyReLU(**data)
