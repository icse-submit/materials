import pickle
import mxnet
data = pickle.load(open('3aa358448394780deb3fc019baad787a19a9f56e.p', 'rb'))
mxnet.ndarray.op.LeakyReLU(**data)
