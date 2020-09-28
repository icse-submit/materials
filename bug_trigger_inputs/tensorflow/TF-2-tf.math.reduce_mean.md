# Bug TF-2
### Function
* [`tf.math.reduce_mean`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/math/reduce_mean)`(input_tensor, axis=None, keepdims=False, name=None)`
### Status
New 
### Resolution
Fixed
### Sympton
Hang and Incorrect Functionality
uint32 & uint64 had been omitted from TF_CALL_INTEGRAL_TYPES
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/2
### Minimal Code to Reproduce
~~~python
input_tensor = np.arange(15).astype('uint64')  # also occurs for 'uint32'
tf.math.reduce_mean(input_tensor, axis=axis)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/2
