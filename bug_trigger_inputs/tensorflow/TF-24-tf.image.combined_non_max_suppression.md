# Bug TF-24
### Function
* [`tf.image.combined_non_max_suppression`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/image/combined_non_max_suppression)`(boxes, scores, max_output_size_per_class, max_total_size, iou_threshold=0.5,  score_threshold=float('-inf'), pad_per_class=False, clip_boxes=True, name=None)`
### Status
New
### Resolution
Reported
### Sympton
Crash(Abort, Segfault)
happens due to large 'max_total_size' . In 2.1.0, it causes what():  vector::_M_fill_insert error Aborted, but in nightly it caseus a segfault. So, reported the issue as segfault
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/24
### Minimal Code to Reproduce
~~~python
tf.image.combined_non_max_suppression(boxes=tf.ones((11,8,2,4)), scores=tf.ones((11,8,2)), max_output_size_per_class=5, max_total_size=311452676677046672)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/24
