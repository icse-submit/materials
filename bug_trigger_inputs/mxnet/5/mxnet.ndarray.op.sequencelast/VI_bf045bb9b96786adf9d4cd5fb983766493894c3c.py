import pickle
import mxnet
data = pickle.load(open('bf045bb9b96786adf9d4cd5fb983766493894c3c.p', 'rb'))
res = mxnet.ndarray.op.SequenceLast(**data)
print(res)
