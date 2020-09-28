import pickle
import tensorflow
data = pickle.load(open('7b711649bd9c9eae243b3a675abbca8d751961f9.p', 'rb'))
tensorflow.dynamic_partition(**data)
