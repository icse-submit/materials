import pickle
import torch
data = pickle.load(open('6af6c5deb7ed4abb31867bcdb5c51989132ac2d1.p', 'rb'))
torch.cholesky_solve(**data)
