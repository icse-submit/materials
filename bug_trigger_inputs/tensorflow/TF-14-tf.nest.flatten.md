# Bug TF-14
### Function
* [`tf.nest.flatten`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nest/flatten)`(structure, expand_composites=False)`
### Status
New
### Resolution
Fixed
### Sympton
Crash (abort,SystemError)
tf.nest.flatten crashes (abort) when expand_composites is 0D boolean is violated.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/14
### Minimal Code to Reproduce
~~~python

tf.nest.flatten(structure = np.zeros((1)), expand_composites=tf.ones((2)))
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/14
