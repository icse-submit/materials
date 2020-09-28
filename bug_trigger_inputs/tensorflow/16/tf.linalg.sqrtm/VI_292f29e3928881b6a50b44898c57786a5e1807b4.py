import pickle
import tensorflow
data = pickle.load(open('292f29e3928881b6a50b44898c57786a5e1807b4.p', 'rb'))
tensorflow.linalg.sqrtm(**data)
