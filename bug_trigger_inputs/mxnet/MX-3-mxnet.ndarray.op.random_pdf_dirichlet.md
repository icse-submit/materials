# Bug MX-3
### Function
* [`mxnet.ndarray.op.random_pdf_dirichlet`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/op/index.html#mxnet.ndarray.op.random_pdf_dirichlet)`(sample=None, alpha=None, is_log=_Null, out=None, name=None, **kwargs)`
* [`mxnet.ndarray.random_pdf_dirichlet`](https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.random_pdf_dirichlet)`(sample=None, alpha=None, is_log=_Null, out=None, name=None, **kwargs)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Floating-point exception)
mxnet.ndarray.op.random_pdf_dirichlet has floating point exception when given sample's shape has 0. Please see the provided code as example.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/mxnet/3
### Minimal Code to Reproduce
~~~python
sample = mxnet.nd.array(np.random.rand(4,0))
alpha = mxnet.nd.array(np.random.rand(1))
mxnet.ndarray.op.random_pdf_dirichlet(sample=sample, alpha=alpha)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/mxnet/3
