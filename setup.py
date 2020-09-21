from setuptools import setup, find_packages
import os
import sys

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
        name='atspy',
        version='0.2.6',
        description='Automated Time Series in Python',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/jroakes/atspy.git',
        author='snowde',
        author_email='d.snow@firmai.org',
        license='MIT',
        packages=find_packages(),
        install_requires=install_requires,
        python_requires=">=3",
        include_package_data=True,
        zip_safe=False
      )
