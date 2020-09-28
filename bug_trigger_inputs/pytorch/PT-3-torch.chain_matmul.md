# Bug PT-3
### Function
* [`torch.chain_matmul`](https://pytorch.org/docs/master/generated/torch.chain_matmul.html)`(*matrices)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Segfault)
empty input caused segmentation fault. The same empty input did not cause any error on another API (torch.broadcast_tensors)
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/3
### Minimal Code to Reproduce
~~~python
torch.chain_matmul()
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/3
