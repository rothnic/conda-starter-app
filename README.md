conda-starter-app
---
A template project to get started with an app that is ready to develop, test, and deploy using [docker](https://www.docker.com/) and [conda](http://conda.pydata.org/docs/intro.html).

This project minimizes external dependencies, with the only hard dependency being either a miniconda install, or docker. Fabric (python) is used both on the host machine and docker images to automate some of the tasks, so is recommended.

**benefits of this starter**
* reproducible dev, test, and execution
* relatively small for a python docker image
* uses conda, so no unnecessary recompilation, access to any python version
* optimized dockerfiles for very fast rebuilds
* setup with tests and linting (pep8)
* includes conda recipe if it will be redistributed via conda

## quickstart

**dependencies**
* install docker
  * boot2docker for osx: `brew install boot2docker`
* install [miniconda](http://conda.pydata.org/miniconda.html)
* `conda install fabric`

**setup**
* `boot2docker up`
* `fab --list` for all available commands

**start**
* `fab test` (builds all required images, tests, and lints the app)
* change a test dependency, e.g. `touch ./tests/my_tests.py`
* `fab test` (runs much quicker, no reinstall of runtime requirements)

## miniconda-starter
Example application for getting started with deploying conda apps. Since conda is a higher-level package manager compared to pip, we use it to handle pre-built binaries for libraries that only introduce risk by compiling ourselves. This app is just a placeholder.

## docker
Utilizes a minimized miniconda docker image, [tinyconda](https://github.com/rothnic/docker-tinyconda) (~200MB vs ~750MB for docker/python). The benefit is that it uses debian, so it is fairly small and compatible with glibc binaries (unlike busybox, alpine), and conda can install pre-built versions of any python version on anaconda.org, which is useful for testing. This balances practicality, size, speed, flexibility, and functionality.

### images
Utilizes two docker images, one for running the app, and one for testing. The dockerfiles have been optimized so that the entire dependency tree `debian->tinyconda->runner image->tester image` is efficiently managed through careful ordering of `COPY` and `RUN` statements.

This means that you don't re-download dependencies, unless you absolutely need to. So, if you are modifying tests, the image for running the app is not rebuilt, due to docker caching.

The built image for the example app is ~320MB, and the testing image is ~327MB.

### building dependencies
For some rare cases, you might need one additional dockerfile for building a dependency, if it requires compilation, and isn't available via conda. This could be pre-built and used directly, or built and uploaded to anaconda.org in a custom channel.

## dependency management
For things that are not on conda, you could build a conda package, or you could just use pip. This project bridges the best of both through a simple command line utility, for managing the requirements in a single requirements.yaml file, instead of having multiple requirements.txt files.

You can install dependencies with requirements.txt via conda using `conda install --file=requirements.txt`, but all dependencies must be available on conda. Instead, the requirements.yaml handles conda and pip requirements separately, allowing the Fabric commands the ability to automate the installation.

## commands
```
build         Build the application docker image.
build_test    Build the docker image for testing the application.
clean_conda   Remove all cached files from conda.
git_tag       Update the project revision and push to git repo.
install_dev   Install app development requirements for conda then pip.
install_run   Install app runtime requirements for conda then pip.
install_test  Install app runtime requirements for conda then pip.
run           Build the app image, run it, then destroy the resulting container.
test          Build the app image, build the test image, then run the test image.
```
