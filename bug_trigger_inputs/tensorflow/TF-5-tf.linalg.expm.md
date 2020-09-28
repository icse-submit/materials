# Bug TF-5
### Function
* [`tf.linalg.expm`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/expm)`(input, name=None)`
### Status
New 
### Resolution
Reproduced
### Sympton
Hang
input big enough to cause reduce_sum to return infinite loop
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/5
### Minimal Code to Reproduce
~~~python
# an input big enough to cause reduce_sum to return inf
in_tensor = (np.random.rand(1000, 1000) * 10000).astype('float16')
tf.linalg.expm(in_tensor) # will not terminate
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/5
