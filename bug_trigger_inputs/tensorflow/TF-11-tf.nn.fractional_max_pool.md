# Bug TF-11
### Function
* [`tf.nn.fractional_max_pool`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nn/fractional_max_pool)`(value, pooling_ratio, pseudo_random=False, overlapping=False, seed=0, name=None)`
### Status
New
### Resolution
Reproduced
### Sympton
Crash (Floating-point exception)
Document says the first and last element of 'pooling_ratio' should be 1.0. If this is violated, floating point exception occurs. 
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/11
### Minimal Code to Reproduce
~~~python
tensor_4D = ...
pooling_ratio = [2.1]

tf.nn.fractional_max_pool(tensor_4D, pooling_ratio)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/11
