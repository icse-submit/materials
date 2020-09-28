# Bug PT-4
### Function
* [`torch.as_strided`](https://pytorch.org/docs/stable/generated/torch.as_strided.html#torch.as_strided)`(input, size, stride, storage_offset=0)`
### Status
Known
### Resolution
Fixed (nightly)
### Sympton
Crash (Segfault)
same as title
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/4
### Minimal Code to Reproduce
~~~python
torch.as_strided(input=torch.tensor([1,2,3]), size=(1,0), stride=(), storage_offset=1)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/4
