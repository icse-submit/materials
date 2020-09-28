# Bug MX-7
### Function
* [`mxnet.ndarray.op.sequencereverse`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.SequenceReverse)`(data=None, sequence_length=None, use_sequence_length=_Null, axis=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.sequencereverse`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.SequenceReverse)`(data=None, sequence_length=None, use_sequence_length=_Null, axis=_Null, out=None, name=None, **kwargs)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Floating-point exception)
mxnet.ndarray.op.SequenceReverse has floating point exception when given data has 0 in its shape. Please see the provided code for example.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/7
### Minimal Code to Reproduce
~~~python
data = mxnet.nd.array(np.random.rand(0,1,1))
mxnet.ndarray.op.SequenceReverse(data)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/7
