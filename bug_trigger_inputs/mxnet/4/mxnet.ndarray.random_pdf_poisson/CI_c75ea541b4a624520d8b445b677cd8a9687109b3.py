import pickle
import mxnet
data = pickle.load(open('c75ea541b4a624520d8b445b677cd8a9687109b3.p', 'rb'))
mxnet.ndarray.random_pdf_poisson(**data)
