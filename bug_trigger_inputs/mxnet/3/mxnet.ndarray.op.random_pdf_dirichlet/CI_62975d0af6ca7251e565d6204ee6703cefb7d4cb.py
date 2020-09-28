import pickle
import mxnet
data = pickle.load(open('62975d0af6ca7251e565d6204ee6703cefb7d4cb.p', 'rb'))
mxnet.ndarray.op.random_pdf_dirichlet(**data)
