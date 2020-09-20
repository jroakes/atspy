import platform
import sys
import os
import os.path
from pkg_resources import normalize_path, working_set, add_activation_listener, require
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
from typing import List

PLATFORM = "unix"
if platform.platform().startswith("Win"):
    PLATFORM = "win"

MODEL_DIR = os.path.join("atspy", "stan", PLATFORM)
MODEL_TARGET_DIR = os.path.join("atspy", "fbprophet", "stan_model")


def get_backends_from_env():
    from fbprophet.models import StanBackendEnum

    return os.environ.get("STAN_BACKEND", StanBackendEnum.PYSTAN.name).split(",")


def build_models(target_dir):
    from fbprophet.models import StanBackendEnum

    for backend in get_backends_from_env():
        StanBackendEnum.get_backend_class(backend).build_model(target_dir, MODEL_DIR)


class BuildPyCommand(build_py):
    """Custom build command to pre-compile Stan models."""

    def run(self):
        if not self.dry_run:
            target_dir = os.path.join(self.build_lib, MODEL_TARGET_DIR)
            self.mkpath(target_dir)
            build_models(target_dir)

        build_py.run(self)


with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="atspy with fbprophet",
    version="0.2.6.1",
    description="Automated Time Series in Python (Includes FB Prophet)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jroakes/atspy.git",
    author="snowde",
    author_email="d.snow@firmai.org",
    packages=find_packages(),
    license="MIT",
    setup_requires=[],
    install_requires=install_requires,
    python_requires=">=3",
    include_package_data=True,
    cmdclass={"build_py": BuildPyCommand},
    zip_safe=False,
)
