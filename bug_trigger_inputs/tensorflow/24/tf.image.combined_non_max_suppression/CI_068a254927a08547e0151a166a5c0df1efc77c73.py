import pickle
import tensorflow
data = pickle.load(open('068a254927a08547e0151a166a5c0df1efc77c73.p', 'rb'))
tensorflow.image.combined_non_max_suppression(**data)
