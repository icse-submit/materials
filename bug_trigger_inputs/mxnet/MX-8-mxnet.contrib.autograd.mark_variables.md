# Bug MX-8
### Function
* [`mxnet.contrib.autograd.mark_variables`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/contrib/autograd/index.html#mxnet.contrib.autograd.mark_variables)`(variables, gradients, grad_reqs='write')`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Segfault)
mx.contrib.autograd.mark_variables throws segmentation fault when variables and gradients are ndarray
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/8
### Minimal Code to Reproduce
~~~python
mx.contrib.autograd.mark_variables(variables=mx.nd.ones((2)), gradients=mx.nd.ones((1)))
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/8
