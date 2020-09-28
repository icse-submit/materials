import pickle
import tensorflow
data = pickle.load(open('7eabed185dae7a8dc3ca1b9ea56e9a49f66cc324.p', 'rb'))
tensorflow.nest.flatten(**data)
