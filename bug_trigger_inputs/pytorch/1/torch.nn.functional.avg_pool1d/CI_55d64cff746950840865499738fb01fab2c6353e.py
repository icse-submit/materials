import pickle
import torch
data = pickle.load(open('55d64cff746950840865499738fb01fab2c6353e.p', 'rb'))
torch.nn.functional.avg_pool1d(**data)
