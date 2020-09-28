import pickle
import mxnet
data = pickle.load(open('fd52036a61d1368a46cd9d0d3f33d8112492b011.p', 'rb'))
mxnet.ndarray.unravel_index(**data)
