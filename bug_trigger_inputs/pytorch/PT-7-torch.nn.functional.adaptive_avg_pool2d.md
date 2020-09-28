# Bug PT-7
### Function
* [`torch.nn.functional.adaptive_avg_pool2d`](https://pytorch.org/docs/stable/nn.functional.html#torch.nn.functional.adaptive_avg_pool2d)`(input, output_size)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Segfault)
when passing a large value and 'input' is valid tensor
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/7
### Minimal Code to Reproduce
~~~python
torch.nn.functional.adaptive_avg_pool2d(torch.randn([2,2,2,2]), 9132760301568586890)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/7
