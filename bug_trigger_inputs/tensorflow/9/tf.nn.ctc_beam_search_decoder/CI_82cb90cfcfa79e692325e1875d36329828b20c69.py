import pickle
import tensorflow
data = pickle.load(open('82cb90cfcfa79e692325e1875d36329828b20c69.p', 'rb'))
tensorflow.nn.ctc_beam_search_decoder(**data)
