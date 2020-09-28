import pickle
import mxnet
data = pickle.load(open('0631de49df8fe72d058cb215a069ae0f550d7555.p', 'rb'))
mxnet.ndarray.random_pdf_dirichlet(**data)
