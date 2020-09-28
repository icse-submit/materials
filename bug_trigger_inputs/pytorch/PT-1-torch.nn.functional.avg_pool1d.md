# Bug PT-1
### Function
* [`torch.nn.functional.avg_pool1d`](https://pytorch.org/docs/stable/nn.functional.html#torch.nn.functional.avg_pool1d)`(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)`
### Status
New
### Resolution
Fixed
### Sympton
Crash (Floating-point exception)
float point exception when stride=0
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/1
### Minimal Code to Reproduce
~~~python
input = torch.tensor(np.random.rand(10, 3, 20, 20))
kernel_size = 4
torch.nn.functional.avg_pool1d(input, kernel_size, stride=0)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/1
