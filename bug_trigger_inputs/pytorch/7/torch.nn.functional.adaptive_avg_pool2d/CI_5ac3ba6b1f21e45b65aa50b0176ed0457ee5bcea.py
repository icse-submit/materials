import pickle
import torch
data = pickle.load(open('5ac3ba6b1f21e45b65aa50b0176ed0457ee5bcea.p', 'rb'))
torch.nn.functional.adaptive_avg_pool2d(**data)
