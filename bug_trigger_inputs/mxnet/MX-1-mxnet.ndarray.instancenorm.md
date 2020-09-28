# Bug MX-1
### Function
* [`mxnet.ndarray.instancenorm`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.InstanceNorm)`(data=None, gamma=None, beta=None, eps=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.op.instancenorm`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.InstanceNorm)`(data=None, gamma=None, beta=None, eps=_Null, out=None, name=None, **kwargs)`
### Status
New
### Resolution
Fixed
### Sympton
Crash (Floating-point exception)
mxnet.ndarray.InstanceNorm has floating point exception when the given data's batch = 0 or channel = 0. Please see the provided code snippets for example.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/1
### Minimal Code to Reproduce
~~~python
input = mxnet.nd.array(np.random.rand(0,1,1))
gamma = mxnet.nd.array(np.random.rand(1))
beta = mxnet.nd.array(np.random.rand(1))
mxnet.ndarray.InstanceNorm(input, gamma, beta)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/1
