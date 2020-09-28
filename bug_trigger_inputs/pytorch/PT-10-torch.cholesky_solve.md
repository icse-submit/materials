# Bug PT-10
### Function
* [`torch.cholesky_solve`](https://pytorch.org/docs/stable/generated/torch.cholesky_solve.html#torch.cholesky_solve)`(input, input2, upper=False, out=None)`
### Status
New
### Resolution
Fixed (PR)
### Sympton
Abort+segfault
The API outputs segfault and several kinds of abort in both nightly version and 1.5.0. There are: munmap_chunk(): invalid pointer, double free or corruption (!prev), corrupted double-linked list, free(): invalid pointer, realloc(): invalid next size
### Constraints
https://github.com/icse-submit/materials/tree/master/constraints/pytorch/10
### Minimal Code to Reproduce
~~~python
torch.cholesky_solve(input=torch.ones([5, 1, 1]), input2 =torch.ones([7, 1,1]), out=torch.ones([1]))
torch.cholesky_solve(input=torch.ones([5,3,5,1]), input2 = torch.ones([10,5,5,5]), out=torch.ones([1]))
torch.cholesky_solve(input=torch.ones([5,3,8,1]), input2 = torch.ones([10,5,8,8]), out=torch.zeros([1]))
torch.cholesky_solve(input=torch.ones([5,2,1]), input2 = torch.ones([10,2,2]), out=torch.ones([1]))
torch.cholesky_solve(input=torch.zeros ([1,1,1]), input2=torch.zeros ([1,4,1,1]), out=torch.zeros([1]))
~~~
### Generated Input to Reproduce
https://github.com/icse-submit/materials/tree/master/bug_trigger_inputs/pytorch/10
