import pickle
import tensorflow
data = pickle.load(open('66fa23e9a5d8c1b254726935284ac7b6cbd643f1.p', 'rb'))
tensorflow.linalg.cholesky_solve(**data)
