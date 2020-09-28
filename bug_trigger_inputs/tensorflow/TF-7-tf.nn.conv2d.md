# Bug TF-7
### Function
* [`tf.nn.conv2d`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/nn/conv2d)`(input, filters, strides, padding, data_format='NHWC', dilations=None, name=None)`
### Status
New
### Resolution
Reproduced
### Sympton
Crash (Floating-point exception)
tf.nn.conv2d crashes(Floating_Point_Exception) when any of the first three dimensions of filters.shape(4D) is 0
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/7
### Minimal Code to Reproduce
~~~python
tf.nn.conv2d(input=tf.ones((1,1,1,1)), filters=tf.ones((0,1,1,1)), strides=1, padding='SAME')
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/7
