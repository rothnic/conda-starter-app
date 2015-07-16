"""Implements tasks for conda app development."""

import yaml
from fabric.api import local

def _install_req_list(base, args='', fields=()):
    with open('./requirements.yaml', 'r') as f:
        settings = yaml.load(f)

        reqs = settings
        for field in fields:
            reqs = reqs.get(field, None)

        if reqs:
            local(base + ' ' + args + ' ' + ' '.join(reqs))
        else:
            print('Nothing configured in requirements.yaml for ' + '->'.join(fields))
        print ''

def install_run():
    """Install app runtime requirements for conda then pip."""
    _install_req_list('conda install', fields=('conda', 'run'))
    _install_req_list('pip install', fields=('pip', 'run'))

def install_dev():
    """Install app development requirements for conda then pip."""
    install_run()
    _install_req_list('conda install', fields=('conda', 'dev'))
    _install_req_list('pip install', fields=('pip', 'dev'))

def install_test():
    """Install app runtime requirements for conda then pip."""
    install_run()
    _install_req_list('conda install', fields=('conda', 'test'))
    _install_req_list('pip install', fields=('pip', 'test'))

def build():
    """Build the application docker image."""
    local('docker build -t example_conda_app .')

def run():
    """Build the app image, run it, then destroy the resulting container."""
    build()
    local('docker run --rm example_conda_app')

def build_test():
    """Build the docker image for testing the application."""
    local('docker build -t example_conda_app_tester -f ./tests/Dockerfile .')

def test():
    """Build the app image, build the test image, then run the test image."""
    build()
    build_test()
    local('docker run --rm example_conda_app_tester')

def clean_conda():
    """Remove all cached files from conda."""
    local('conda clean --yes --tarballs --packages')

def git_tag(tag):
    """Update the project revision and push to git repo."""
    local('git tag ' + str(tag))
    local('git push --tags')
