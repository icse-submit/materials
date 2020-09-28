import pickle
import mxnet
data = pickle.load(open('6dda1c52b42fefe9c30cde351586f5d98a1ab06f.p', 'rb'))
mxnet.ndarray.op.InstanceNorm(**data)
