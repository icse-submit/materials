import pickle
import tensorflow
data = pickle.load(open('c23f4e8804a300f6c09af06034d6387bc9382e02.p', 'rb'))
tensorflow.linalg.expm(**data)
