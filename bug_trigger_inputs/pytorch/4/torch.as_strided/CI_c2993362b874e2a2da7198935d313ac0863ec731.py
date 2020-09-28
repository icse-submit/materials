import pickle
import torch
data = pickle.load(open('c2993362b874e2a2da7198935d313ac0863ec731.p', 'rb'))
torch.as_strided(**data)
