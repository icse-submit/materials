# Bug TF-8
### Function
* [`tf.dynamic_partition`](https://www.tensorflow.org/versions/r2.1/api_docs/python/tf/dynamic_partition)`(data, partitions, num_partitions, name=None)`
### Status
New 
### Resolution
Reproduced
### Sympton
Other (High memory consumption and process killed)
High memory consumption. Killed after a while. Happens due to large 'num_partitions'
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/tensorflow/8
### Minimal Code to Reproduce
~~~python
partitions = [0, 0, 1, 1, 0]
num_partitions = 100000000 
data = [10, 20, 30, 40, 50]

output = tf.dynamic_partition(data, partitions, num_partitions)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/tensorflow/8
