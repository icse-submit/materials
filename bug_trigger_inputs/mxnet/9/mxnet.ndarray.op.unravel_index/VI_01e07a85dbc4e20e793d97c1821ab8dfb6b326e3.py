import pickle
import mxnet
data = pickle.load(open('01e07a85dbc4e20e793d97c1821ab8dfb6b326e3.p', 'rb'))
res = mxnet.ndarray.op.unravel_index(**data)
print(res)
