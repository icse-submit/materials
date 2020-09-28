# Bug TF-3
### Function
* [`tf.image.crop_and_resize`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/image/crop_and_resize)`(image, boxes, box_indices, crop_size, method='bilinear', extrapolation_value=0, name=None)`
### Status
New
### Resolution
Fixed (PR)
### Sympton
Crash (Segfault)
tf.image.crop_and_resize segfault when there is a very large value in boxes. Can also be reproduced in nightly version
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/3
### Minimal Code to Reproduce
~~~python
tf.image.crop_and_resize(image=tf.zeros((2,1,1,1)), boxes=[[1.0e+40, 0,0,0]], box_indices=[1], crop_size=[1,1])
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/3
