import pickle
import tensorflow
data = pickle.load(open('eaeb7702b7facf880e622ce82a9770af0eda2e18.p', 'rb'))
tensorflow.linalg.matrix_rank(**data)
