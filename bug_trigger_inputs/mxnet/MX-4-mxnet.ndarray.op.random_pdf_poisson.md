# Bug MX-4
### Function
* [`mxnet.ndarray.op.random_pdf_poisson`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.random_pdf_poisson)`(sample=None, lam=None, is_log=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.random_pdf_poisson`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.random_pdf_poisson)`(sample=None, lam=None, is_log=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.random_pdf_exponential`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.random_pdf_exponential)`(sample=None, lam=None, is_log=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.op.random_pdf_exponential`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.random_pdf_exponential)`(sample=None, lam=None, is_log=_Null, out=None, name=None, **kwargs)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Floating-point exception)
mxnet.ndarray.op.random_pdf_poisson has floating point exception when given lam is shape (0,). Please see the provided code snippet for example.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/4
### Minimal Code to Reproduce
~~~python
lam = mxnet.nd.array(np.random.rand(0))
sample = mxnet.nd.array(np.random.rand(2))
mxnet.ndarray.op.random_pdf_poisson(sample=sample, lam=lam)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/4
