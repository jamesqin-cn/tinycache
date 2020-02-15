#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "tinycache",
    version = "0.1.3",
    author = "jamesqin",
    author_email = "jamesqin@vip.qq.com",
    description = "tinycache a python modules base on local file for any python data struct",
    long_description = long_description,
    long_description_content_type="text/markdown",
    license = "MIT",
    url = "https://github.com/jamesqin-cn/tinycache",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
