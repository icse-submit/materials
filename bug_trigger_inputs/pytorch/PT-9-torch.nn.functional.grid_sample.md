# Bug PT-9
### Function
* [`torch.nn.functional.grid_sample`](https://pytorch.org/docs/stable/nn.functional.html#torch.nn.functional.grid_sample)`(input, grid, mode='bilinear', padding_mode='zeros', align_corners=None)`
### Status
New
### Resolution
Fixed
### Sympton
Crash (Segfault)
This bug only occurs when padding_mode is 'reflection', and when the first element in grid is very large.
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/9
### Minimal Code to Reproduce
~~~python
torch.nn.functional.grid_sample(input= torch.zeros([1,1,1,3]), grid=torch.tensor([[[[ 2.3e+38, 0]]]]) , padding_mode='reflection')
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/9
