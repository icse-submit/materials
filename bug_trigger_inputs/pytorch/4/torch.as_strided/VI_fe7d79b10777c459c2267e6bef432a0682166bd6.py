import pickle
import torch
data = pickle.load(open('fe7d79b10777c459c2267e6bef432a0682166bd6.p', 'rb'))
torch.as_strided(**data)
