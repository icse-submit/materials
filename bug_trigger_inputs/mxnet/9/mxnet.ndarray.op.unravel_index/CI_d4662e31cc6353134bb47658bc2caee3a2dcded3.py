import pickle
import mxnet
data = pickle.load(open('d4662e31cc6353134bb47658bc2caee3a2dcded3.p', 'rb'))
res = mxnet.ndarray.op.unravel_index(**data)
print(res)
