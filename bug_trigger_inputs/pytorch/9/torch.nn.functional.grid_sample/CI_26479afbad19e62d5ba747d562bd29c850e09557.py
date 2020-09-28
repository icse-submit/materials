import pickle
import torch
data = pickle.load(open('26479afbad19e62d5ba747d562bd29c850e09557.p', 'rb'))
torch.nn.functional.grid_sample(**data)
