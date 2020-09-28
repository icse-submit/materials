import pickle
import torch
data = pickle.load(open('e35aa2f1a6809210f89b2711bad4fde1647d27b3.p', 'rb'))
torch.cholesky_solve(**data)
