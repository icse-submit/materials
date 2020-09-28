import pickle
import torch
data = pickle.load(open('6f41cbad449ae42078dc5f717a67d94ef824a8aa.p', 'rb'))
torch.nn.functional.adaptive_avg_pool3d(**data)
