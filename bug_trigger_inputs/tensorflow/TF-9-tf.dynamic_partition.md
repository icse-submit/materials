# Bug TF-9
### Function
* [`tf.dynamic_partition`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/dynamic_partition)`(data, partitions, num_partitions, name=None)`
* [`tf.keras.backend.ctc_decode`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/keras/backend/ctc_decode)`(y_pred, input_length, greedy=True, beam_width=100, top_paths=1)`
* [`tf.nn.ctc_beam_search_decoder`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nn/ctc_beam_search_decoder)`(inputs, sequence_length, beam_width=100, top_paths=1)`
* [`tf.split`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/split)`(value, num_or_size_splits, axis=0, num=None, name='split')`
* [`tf.unstack`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/unstack)`(value, num=None, axis=0, name='unstack')`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (bad_alloc)
when top_paths is large and greedy is False
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/9
### Minimal Code to Reproduce
~~~python
tf.keras.backend.ctc_decode(y_pred=tf.ones((1,1,1)), input_length=1, top_paths=1000000000, greedy=False)
tf.nn.ctc_beam_search_decoder(inputs=tf.ones((1,1,1)), sequence_length=[1], top_paths=1000000000000)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/9
