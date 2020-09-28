import pickle
import tensorflow
data = pickle.load(open('66090171b5ba4523a8fb8eadb38e1916acfa71e8.p', 'rb'))
tensorflow.summary.flush(**data)
