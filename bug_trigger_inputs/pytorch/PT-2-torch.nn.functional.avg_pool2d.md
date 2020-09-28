# Bug PT-2
### Function
* [`torch.nn.functional.avg_pool2d`](https://pytorch.org/docs/stable/nn.functional.html#torch.nn.functional.avg_pool2d)`(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)`
### Status
New
### Resolution
Fixed
### Sympton
Crash (Floating-point exception)
float point exception when stride=0
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/2
### Minimal Code to Reproduce
~~~python
input = torch.tensor(np.random.rand(10, 3, 20, 20))
kernel_size = 4
torch.nn.functional.avg_pool2d(input, kernel_size, stride=0)
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/2
