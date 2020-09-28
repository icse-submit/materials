# Bug TF-4
### Function
* [`tf.nn.space_to_depth`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nn/space_to_depth)`(input, block_size, data_format='NHWC', name=None)`
* [`tf.nn.depth_to_space`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nn/depth_to_space)`(input, block_size, data_format='NHWC', name=None)`
### Status
New
### Resolution
Reproduced
### Sympton
Crash (Segfault)
tf.nn.space_to_depth and tf.nn.depth_to_space crashes (segfault) in when input is EXACTLY of length 4, block_size>1 and data_format=NCHW_VECT_C.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/4
### Minimal Code to Reproduce
~~~python
tf.nn.space_to_depth(input=tf.zeros((4)), block_size = 2, data_format ='NCHW_VECT_C')
tf.nn.depth_to_space(input=tf.zeros((4)), block_size = 2, data_format ='NCHW_VECT_C')
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/4
