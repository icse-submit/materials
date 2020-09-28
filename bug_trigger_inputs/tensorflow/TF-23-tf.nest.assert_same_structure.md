# Bug TF-23
### Function
* [`tf.nest.assert_same_structure`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nest/assert_same_structure)`(nest1, nest2, check_types=True, expand_composites=False)`
### Status
New
### Resolution
Fixed
### Sympton
Crash (abort,SystemError)
tf.nest.assert_same_structure crashes (abort, systemerror) when some either check_types or expand_composites is 0d bool is violated.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/23
### Minimal Code to Reproduce
~~~python
tf.nest.assert_same_structure(nest1=np.zeros((1)), nest2=tf.ones((1,1,1)), check_types=tf.ones((2)))
tf.nest.assert_same_structure(nest1=np.zeros((1)), nest2=tf.ones((1,1,1)), expand_composites=tf.ones((2)))
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/23
