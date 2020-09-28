import pickle
import mxnet
data = pickle.load(open('8a2bc1ddc3709aa913b60493f545b65e912488c4.p', 'rb'))
mxnet.ndarray.op.random_pdf_poisson(**data)
