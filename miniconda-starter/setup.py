from setuptools import setup
import versioneer

setup (
    name             = "example_conda_app",
    version          = versioneer.get_version(),
    cmdclass         = versioneer.get_cmdclass(),
    description      = "Example application to be deployed.",
    packages         = ["example_conda_app"],
    entry_points     = {'console_scripts':
                        ['run-the-app = example_conda_app:main']}
)
