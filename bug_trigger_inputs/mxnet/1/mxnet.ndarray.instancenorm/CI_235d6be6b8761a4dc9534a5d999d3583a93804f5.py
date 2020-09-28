import pickle
import mxnet
data = pickle.load(open('235d6be6b8761a4dc9534a5d999d3583a93804f5.p', 'rb'))
mxnet.ndarray.InstanceNorm(**data)
