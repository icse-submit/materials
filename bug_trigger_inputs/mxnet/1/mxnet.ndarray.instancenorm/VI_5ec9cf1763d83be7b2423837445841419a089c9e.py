import pickle
import mxnet
data = pickle.load(open('5ec9cf1763d83be7b2423837445841419a089c9e.p', 'rb'))
mxnet.ndarray.InstanceNorm(**data)
