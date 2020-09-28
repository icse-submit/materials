# Constraints for the Library Bugs DocTer Found
### Content
* This folder contains the extracted constraints for the library bugs found in 3 DL libraries (tensorflow, pytorch, mxnet).
* The folder structure has correspondence to the BugID in the Library Bug List (e.g., Bug MX-1 corresponds to the `mxnet/1` folder).
* The extracted constraints are represented using YAML files.
* The `descp` and `doc_dtype` fields in each YAML file are not used for fuzzing,
  but it's preserved here to provide a one-stop view of the original document content.

### Example
Here is an example to illustrate how to look at the extracted constraints:

Under `mxnet/1` folder, let's take a look at [mxnet.ndarray.instancenorm.yaml](https://github.com/icse-submit/materials/blob/master/constraints/mxnet/1/mxnet.ndarray.instancenorm.yaml)

At the bottom of the file:
```
link: https://mxnet.apache.org/versions/1.6/api/python/docs/api/ndarray/ndarray.html#mxnet.ndarray.InstanceNorm
package: mxnet
target: InstanceNorm
title: mxnet.ndarray.InstanceNorm
version: 1.6.0
```
This presents some general information about the API `mxnet.ndarray.InstanceNorm`, where we are testing MXNet version `1.6.0`.
`link` tells where the original API document is, so we can compare the information presented in the original API document and extracted constraints.

Under `inputs` section:
```
inputs:
  optional:
  - data
  - gamma
  - beta
  - eps
  - out
  - name
  required:
  - '**kwargs'
```
This presents the input parameters of the API `mxnet.ndarray.InstanceNorm`.
The parameters are divided into `required` and `optional`.
However, for this particular case, parameter `**kwargs` pass a keyworded, variable-length argument list which is not really required;
and it provides no information what we should generate, so it is ignored during fuzzing.

Under `dependency` section:
```
dependency:
- batch
- channel
```
This section presents the constants/parameters input parameters depend on.
  
Under `constraints` section:
```
constraints:
  '**kwargs':
    descp: ''
  beta:
    default: None
    descp: A vector of length 'channel', which is added to the product of the normalized
      input and the weight.
    doc_dtype:
    - NDArray
    ndim:
    - '1'
    shape:
    - '[channel]'
    structure:
    - ndarray
```
the constraints for each parameter is presented in this section.

For example, in the code block above, the constraints for input parameter `beta` is presented.
We see that the default value for `beta` is `None`.
The number of dimension (`ndim`) is `1` (because the description says it's a **"vector"**).
The `shape` of `beta` is `[channel]` (because the description says it's **"of length channel"**).
The `structure` of `beta` is `ndarray` (because in the orignal document, the parameter section indicates `beta` is of type NDArray).
