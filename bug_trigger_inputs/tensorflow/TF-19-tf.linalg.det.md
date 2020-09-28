# Bug TF-19
### Function
* [`tf.linalg.det`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/det)`(input, name=None)`
* [`tf.linalg.slogdet`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/slogdet)`(input, name=None)`
### Status
Known
### Resolution
Fixed (2.2.0)
### Sympton
Crash (Segfault)
Crash (bad_alloc)

### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/19
### Minimal Code to Reproduce
~~~python
N/A
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/19
