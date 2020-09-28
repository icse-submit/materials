import pickle
import mxnet
data = pickle.load(open('1309ae4493fbadba797b29df57ecaa37d3b5c304.p', 'rb'))
mxnet.ndarray.op.random_pdf_dirichlet(**data)
