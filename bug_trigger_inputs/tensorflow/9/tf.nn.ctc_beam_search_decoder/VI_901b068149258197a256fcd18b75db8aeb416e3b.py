import pickle
import tensorflow
data = pickle.load(open('901b068149258197a256fcd18b75db8aeb416e3b.p', 'rb'))
tensorflow.nn.ctc_beam_search_decoder(**data)
