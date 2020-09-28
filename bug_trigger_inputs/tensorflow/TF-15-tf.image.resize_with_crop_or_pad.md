# Bug TF-15
### Function
* [`tf.image.resize_with_crop_or_pad`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/image/resize_with_crop_or_pad)`(image, target_height, target_width)`
* [`tf.keras.backend.depthwise_conv2d`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/keras/backend/depthwise_conv2d)`(x, depthwise_kernel, strides=(1, 1), padding='valid', data_format=None, dilation_rate=(1, 1))`
* [`tf.keras.backend.zeros`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/keras/backend/zeros)`(shape, dtype=None, name=None)`
* [`tf.linalg.tensor_diag`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/linalg/tensor_diag)`(diagonal, name=None)`
* [`tf.ones`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/ones)`(shape, dtype=tf.dtypes.float32, name=None)`
* [`tf.signal.overlap_and_add`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/signal/overlap_and_add)`(signal, frame_step, name=None)`
### Status
Known
### Resolution
Fixed (2.2.0)
### Sympton
Crash (bad_alloc)
Fixed by using a minimum alignment of 64 bytes when memory allocation would be too large.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/15
### Minimal Code to Reproduce
~~~python
N/A
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/15
