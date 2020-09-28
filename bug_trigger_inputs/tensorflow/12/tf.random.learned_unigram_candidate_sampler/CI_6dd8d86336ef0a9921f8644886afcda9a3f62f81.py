import pickle
import tensorflow
data = pickle.load(open('6dd8d86336ef0a9921f8644886afcda9a3f62f81.p', 'rb'))
tensorflow.random.learned_unigram_candidate_sampler(**data)
