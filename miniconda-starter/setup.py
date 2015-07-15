from setuptools import setup

setup (
    name             = "example_conda_app",
    version          = "0.1",
    description      = "Example application to be deployed.",
    packages         = ["example_conda_app"],
    entry_points     = {'console_scripts':
                        ['run-the-app = example_conda_app:main']}
)
