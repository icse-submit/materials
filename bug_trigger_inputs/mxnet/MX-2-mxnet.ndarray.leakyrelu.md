# Bug MX-2
### Function
* [`mxnet.ndarray.leakyrelu`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.LeakyReLU)`(data=None, gamma=None, act_type=_Null, slope=_Null, lower_bound=_Null, upper_bound=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.op.leakyrelu`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.LeakyReLU)`(data=None, gamma=None, act_type=_Null, slope=_Null, lower_bound=_Null, upper_bound=_Null, out=None, name=None, **kwargs)`
### Status
New
### Resolution
Fixed
### Sympton
Crash (Floating-point exception)
mxnet.ndarray.LeakyReLU has floating point exception when given data's shape contain 0. Please see provided code snippet for example.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/2
### Minimal Code to Reproduce
~~~python
input = mxnet.nd.array(np.random.rand(0,1,1))
mxnet.ndarray.LeakyReLU(input)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/2
