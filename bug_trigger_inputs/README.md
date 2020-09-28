# Bug-triggering Inputs and Drivers
### Content
* This folder contains the bug-triggering input and their driver script for 3 DL libraries (tensorflow, pytorch, mxnet).
* Please build a docker image using the provided `Dockerfile` to try out the bug-triggering input.
* To build the image:
  * Please make sure docker is installed
  * run `docker build -t dl-env .` within the same folder containing this `README.md` (Please note the `.` in the command)
  * The building process will take a couple of minutes.
  * After that, docker image called `dl-env` is built.
* To run the bug-triggering input:
  * run 
  ```
  docker run --rm -it -v /Absolute/path/to/this/folder:/workspace:ro --memory=4g --memory-swap=4g dl-env
  ```
  this commands starts a docker container and mounts the current directory as `/workspace` in the container in read-only mode.
  The memory limitation is 4g which is consistent to our experiment setting.
  * Once in the docker container, please run `try_bugs_in_lib.sh` to try the bugs.

### Bug Triggering Input
* Bug-triggering inputs are stored as pickle files
* For example, under `mxnet/1/mxnet.ndarray.instancenrom`, there are 2 pickle files (`*.p`), and 2 python scripts to load the input and execute the API function with that input.
* The prefix `CI` means `Conforming Input` which our fuzzer generated input by conforming to the constraints, and `VI` means `Violating Input` which our fuzzer tries to violate 1 parameter's constraints.
* To try out the input individually, please `cd` into where the pickle file is located and execute the corresponding python script.
