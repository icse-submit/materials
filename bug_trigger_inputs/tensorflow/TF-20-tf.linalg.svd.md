# Bug TF-20
### Function
* [`tf.linalg.svd`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/svd)`(tensor, full_matrices=False, compute_uv=True, name=None)`
* [`tf.linalg.matrix_rank`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/matrix_rank)`(a, tol=None, validate_args=False, name=None)`
* [`tf.linalg.pinv`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/pinv)`(a, rcond=None, validate_args=False, name=None)`
### Status
Known
### Resolution
Fixed (nightly)
### Sympton
Crash (Segfault)
segfaults when input shape has at least one element being 0.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/20
### Minimal Code to Reproduce
~~~python
tf.linalg.svd(np.random.rand(2, 0)) # segfault
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/20
