import pickle
import mxnet
data = pickle.load(open('cff98127fcab948de25bd18f3471098b9f765c21.p', 'rb'))
mxnet.ndarray.random_pdf_poisson(**data)
