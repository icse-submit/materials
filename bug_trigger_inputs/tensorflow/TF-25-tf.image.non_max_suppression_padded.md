# Bug TF-25
### Function
* [`tf.image.non_max_suppression_padded`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/image/non_max_suppression_padded)`(boxes, scores, max_output_size, iou_threshold=0.5, score_threshold=float('-inf'), pad_to_max_output_size=False, name=None)`
### Status
Known
### Resolution
Fixed (2.2.0)
### Sympton
Crash (bad_alloc)
happens due to large 'max_output_size' 
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/25
### Minimal Code to Reproduce
~~~python
N/A
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/25
