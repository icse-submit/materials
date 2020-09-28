# Bug MX-5
### Function
* [`mxnet.ndarray.op.sequencelast`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.SequenceLast)`(data=None, sequence_length=None, use_sequence_length=_Null, axis=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.sequencelast`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.SequenceLast)`(data=None, sequence_length=None, use_sequence_length=_Null, axis=_Null, out=None, name=None, **kwargs)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Floating-point exception)
mxnet.ndarray.op.SequenceLast has floating point exception when given data's shape containing 0. Please see the provided code for example.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/5
### Minimal Code to Reproduce
~~~python
data = mxnet.nd.array(np.random.rand(1,0,0))
mxnet.ndarray.op.SequenceLast(data)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/5
