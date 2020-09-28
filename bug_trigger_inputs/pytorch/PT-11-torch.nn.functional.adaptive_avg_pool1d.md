# Bug PT-11
### Function
* [`torch.nn.functional.adaptive_avg_pool1d`](https://pytorch.org/docs/stable/nn.functional.html#torch.nn.functional.adaptive_avg_pool1d)`(input, output_size)`
### Status
New
### Resolution
Confirmed
### Sympton
Crash (Segfault)
when passing a large value and 'input' is valid tensor
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/11
### Minimal Code to Reproduce
~~~python
torch.nn.functional.adaptive_avg_pool1d(torch.randn([2,2,2]), 9132760301568586890)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/11
