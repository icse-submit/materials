import pickle
import torch
data = pickle.load(open('dd0eb7901523d494d4aa324f474c782063e9e231.p', 'rb'))
torch.nn.functional.adaptive_avg_pool3d(**data)
