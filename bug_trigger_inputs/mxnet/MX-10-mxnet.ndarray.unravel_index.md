# Bug MX-10
### Function
* [`mxnet.ndarray.unravel_index`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.unravel_index)`(data=None, shape=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.op.unravel_index`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.unravel_index)`(data=None, shape=_Null, out=None, name=None, **kwargs)`
### Status
Known
### Resolution
Fixed (nightly)
### Sympton
Crash (Segfault)

### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/10
### Minimal Code to Reproduce
~~~python
N/A
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/10
