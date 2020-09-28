import pickle
import mxnet
data = pickle.load(open('97bdfa5c4c5d186bccdac3b5b92ff69ff4308e0c.p', 'rb'))
mxnet.ndarray.random_pdf_dirichlet(**data)
