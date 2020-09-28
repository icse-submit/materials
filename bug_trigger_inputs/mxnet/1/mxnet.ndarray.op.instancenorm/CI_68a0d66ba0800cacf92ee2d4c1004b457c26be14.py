import pickle
import mxnet
data = pickle.load(open('68a0d66ba0800cacf92ee2d4c1004b457c26be14.p', 'rb'))
mxnet.ndarray.op.InstanceNorm(**data)
