# Bug TF-17
### Function
* [`tf.linalg.solve`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/solve)`(matrix, rhs, adjoint=False, name=None)`
### Status
Known
### Resolution
Fixed (2.2.0)
### Sympton
Crash (bad_alloc)
All input tensors should have same shape
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/17
### Minimal Code to Reproduce
~~~python
N/A
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/17
