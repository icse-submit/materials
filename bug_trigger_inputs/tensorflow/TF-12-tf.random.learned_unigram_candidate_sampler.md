# Bug TF-12
### Function
* [`tf.random.learned_unigram_candidate_sampler`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/random/learned_unigram_candidate_sampler)`(true_classes, num_true, num_sampled, unique, range_max, seed=None, name=None)`
### Status
Known
### Resolution
Fixed (nightly)
### Sympton
Crash (Segfault)
tf.random.learned_unigram_candidate_sampler crashes(segfault) when true_classes containa large value AND num_true=rank(true_classes)[-1]
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/12
### Minimal Code to Reproduce
~~~python
true_classes = [[1, 100000]]
num_true = 2
tf.random.learned_unigram_candidate_sampler(true_classes=true_classes, num_true=num_true, num_sampled=10, unique=False, range_max=1)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/12
