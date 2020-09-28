# Bug TF-6
### Function
* [`tf.nn.atrous_conv2d`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nn/atrous_conv2d)`(value, filters, rate, padding, name=None)`
### Status
New
### Resolution
Reproduced
### Sympton
Crash (Floating-point exception)
same as titel
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/6
### Minimal Code to Reproduce
~~~python
tf.nn.atrous_conv2d(filters=tf.ones((1,1,0,1)), value=tf.ones((1,1,1,1)), rate=1, padding="SAME")
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/6
