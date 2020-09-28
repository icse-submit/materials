import pickle
import mxnet
data = pickle.load(open('38d7ac059f5ee423d7c28672da7c45ba7dc9c143.p', 'rb'))
res = mxnet.ndarray.unravel_index(**data)
print(res)
