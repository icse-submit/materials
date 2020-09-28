import pickle
import torch
data = pickle.load(open('c7029201de215b99cc1569c873437b3a568d4900.p', 'rb'))
torch.nn.functional.adaptive_avg_pool1d(**data)
