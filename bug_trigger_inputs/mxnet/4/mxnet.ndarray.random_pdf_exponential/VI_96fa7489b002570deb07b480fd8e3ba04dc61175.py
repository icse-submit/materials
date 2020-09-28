import pickle
import mxnet
data = pickle.load(open('96fa7489b002570deb07b480fd8e3ba04dc61175.p', 'rb'))
mxnet.ndarray.random_pdf_exponential(**data)
