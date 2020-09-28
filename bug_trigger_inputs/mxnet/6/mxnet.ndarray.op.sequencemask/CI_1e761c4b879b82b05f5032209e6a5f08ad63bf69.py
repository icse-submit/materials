import pickle
import mxnet
data = pickle.load(open('1e761c4b879b82b05f5032209e6a5f08ad63bf69.p', 'rb'))
mxnet.ndarray.op.SequenceMask(**data)
