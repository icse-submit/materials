import pickle
import mxnet
data = pickle.load(open('3c15c5ae85e16b766d42e7183dc7de1816f01cad.p', 'rb'))
mxnet.ndarray.LeakyReLU(**data)
