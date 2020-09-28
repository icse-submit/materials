# Bug TF-13
### Function
* [`tf.nn.fractional_max_pool`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nn/fractional_max_pool)`(value, pooling_ratio, pseudo_random=False, overlapping=False, seed=0, name=None)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (bad_alloc)
tf.nn.fractional_max_pool aborts when pooling_ratio is negative in tf2.1. It throws segfault in nightly version.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/13
### Minimal Code to Reproduce
~~~python
tf.nn.fractional_max_pool(value=tf.ones((1,1,1,1)), seed=1, pooling_ratio=-1)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/13
