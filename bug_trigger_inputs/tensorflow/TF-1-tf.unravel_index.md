# Bug TF-1
### Function
* [`tf.unravel_index`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/unravel_index)`(indices, dims, name=None)`
### Status
New 
### Resolution
Fixed
### Sympton
Crash (Floating-point exception)
indices in tf.unravel_index should make sure it is not out of boundary compared to dims.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/1
### Minimal Code to Reproduce
~~~python
tf.unravel_index(indices=[2, 5, 7], dims=[3, 0])
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/1
