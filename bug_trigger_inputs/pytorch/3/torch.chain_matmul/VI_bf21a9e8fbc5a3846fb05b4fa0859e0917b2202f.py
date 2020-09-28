import pickle
import torch
data = pickle.load(open('bf21a9e8fbc5a3846fb05b4fa0859e0917b2202f.p', 'rb'))
torch.chain_matmul(**data)
