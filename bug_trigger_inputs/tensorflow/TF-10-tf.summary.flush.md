# Bug TF-10
### Function
* [`tf.summary.flush`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/summary/flush)`(writer=None, name=None)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Segfault)
The API requires 'writer' to be tf.summary.SummaryWriter type, but we didn't extract this constraint, and passes a random tesnor, which causes a segfault.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/10
### Minimal Code to Reproduce
~~~python
tf.summary.flush(writer=np.random.rand(2,2))
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/10
