import pickle
import tensorflow
data = pickle.load(open('146a481fd4162eae247112252ef588f6db1bab93.p', 'rb'))
tensorflow.linalg.solve(**data)
