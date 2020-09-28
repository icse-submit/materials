# Bug PT-5
### Function
* [`torch.nn.functional.adaptive_avg_pool2d`](https://pytorch.org/docs/stable/nn.functional.html#torch.nn.functional.adaptive_avg_pool2d)`(input, output_size)`
### Status
New
### Resolution
Fixed
### Sympton
Crash (Segfault)
a segmentation fault when output_size is an empty array [] and `input` is a valid tensor that API expects
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/5
### Minimal Code to Reproduce
~~~python
torch.nn.functional.adaptive_avg_pool2d(torch.randn([2,2,2,2]), []) 
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/5
