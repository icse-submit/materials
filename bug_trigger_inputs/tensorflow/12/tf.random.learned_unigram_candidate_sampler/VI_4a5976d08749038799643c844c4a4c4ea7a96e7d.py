import pickle
import tensorflow
data = pickle.load(open('4a5976d08749038799643c844c4a4c4ea7a96e7d.p', 'rb'))
tensorflow.random.learned_unigram_candidate_sampler(**data)
