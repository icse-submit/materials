import pickle
import tensorflow
data = pickle.load(open('3e481330c39f6c09ce9111567637cbb282a6d182.p', 'rb'))
tensorflow.ones(**data)
