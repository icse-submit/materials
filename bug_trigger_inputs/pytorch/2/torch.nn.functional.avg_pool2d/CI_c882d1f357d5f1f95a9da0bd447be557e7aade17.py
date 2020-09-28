import pickle
import torch
data = pickle.load(open('c882d1f357d5f1f95a9da0bd447be557e7aade17.p', 'rb'))
torch.nn.functional.avg_pool2d(**data)
