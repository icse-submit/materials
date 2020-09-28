import pickle
import mxnet
data = pickle.load(open('7aae785b18a19cfc4bcefafd0b20b3e27351932a.p', 'rb'))
mxnet.contrib.autograd.mark_variables(**data)
