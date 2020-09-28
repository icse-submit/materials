import pickle
import tensorflow
data = pickle.load(open('c5d533a703464b617fc87ea04c7af88aa26cc095.p', 'rb'))
tensorflow.split(**data)
