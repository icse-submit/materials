# Bug TF-18
### Function
* [`tf.math.unsorted_segment_max`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/math/unsorted_segment_max)`(data, segment_ids, num_segments, name=None)`
* [`tf.math.unsorted_segment_min`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/math/unsorted_segment_min)`(data, segment_ids, num_segments, name=None)`
* [`tf.math.unsorted_segment_prod`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/math/unsorted_segment_prod)`(data, segment_ids, num_segments, name=None)`
* [`tf.math.unsorted_segment_sum`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/math/unsorted_segment_sum)`(data, segment_ids, num_segments, name=None)`
### Status
Known
### Resolution
Fixed (2.2.0)
### Sympton
Crash (bad_alloc)
data' input tesnor is too large. Fixed by handling large input tensor to throw an exception at python-level.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/18
### Minimal Code to Reproduce
~~~python
N/A
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/18
