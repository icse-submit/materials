# Bug MX-9
### Function
* [`mxnet.ndarray.unravel_index`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.unravel_index)`(data=None, shape=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.op.unravel_index`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.unravel_index)`(data=None, shape=_Null, out=None, name=None, **kwargs)`
### Status
Known
### Resolution
Fixed (nightly)
### Sympton
Crash (Floating-point exception)

### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/9
### Minimal Code to Reproduce
~~~python
data = mxnet.nd.array(np.random.rand(1,0,1))
mxnet.ndarray.unravel_index(data=data, shape=(1,1,1,1))
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/9
