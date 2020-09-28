# Bug TF-16
### Function
* [`tf.linalg.cholesky_solve`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/cholesky_solve)`(chol, rhs, name=None)`
* [`tf.linalg.cholesky`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/cholesky)`(input, name=None)`
* [`tf.linalg.eigh`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/eigh)`(tensor, name=None)`
* [`tf.linalg.eigvalsh`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/eigvalsh)`(tensor, name=None)`
* [`tf.linalg.inv`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/inv)`(input, adjoint=False, name=None)`
* [`tf.linalg.logdet`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/logdet)`(matrix, name=None)`
* [`tf.linalg.logm`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/logm)`(input, name=None)`
* [`tf.linalg.sqrtm`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/sqrtm)`(input, name=None)`
* [`tf.linalg.triangular_solve`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/solve)`(matrix, rhs, lower=True, adjoint=False, name=None)`
* [`tf.linalg.solve`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/triangular_solve)`(matrix, rhs, adjoint=False, name=None)`
* [`tf.linalg.qr`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/qr)`(input, full_matrices=False, name=None)`
* [`tf.linalg.svd`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/svd)`(tensor, full_matrices=False, compute_uv=True, name=None)`
### Status
Known
### Resolution
Fixed (2.2.0)
### Sympton
Crash (Segfault)
Crash (bad_alloc)

### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/16
### Minimal Code to Reproduce
~~~python
N/A
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/16
