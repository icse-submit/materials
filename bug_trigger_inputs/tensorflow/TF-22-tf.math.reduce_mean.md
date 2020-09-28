# Bug TF-22
### Function
* [`tf.math.reduce_mean`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/math/reduce_mean)`(input_tensor, axis=None, keepdims=False, name=None)`
* [`tf.math.reduce_variance`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/math/reduce_variance)`(input_tensor, axis=None, keepdims=False, name=None)`
* [`tf.math.reduce_std`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/math/reduce_std)`(input_tensor, axis=None, keepdims=False, name=None)`
### Status
Known
### Resolution
Fixed (2.2.0)
### Sympton
Crash (Floating-point exception)

### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/22
### Minimal Code to Reproduce
~~~python
N/A
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/22
