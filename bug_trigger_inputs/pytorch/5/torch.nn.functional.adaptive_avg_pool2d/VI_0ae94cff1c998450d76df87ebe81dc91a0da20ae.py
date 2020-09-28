import pickle
import torch
data = pickle.load(open('0ae94cff1c998450d76df87ebe81dc91a0da20ae.p', 'rb'))
torch.nn.functional.adaptive_avg_pool2d(**data)
