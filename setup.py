#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name = "tinycache",
    version = "0.1.0",
    author = "jamesqin",
    author_email = "jamesqin@vip.qq.com",
    description = "filecache is a python modules base on local file for any python data struct",
    long_description = "filecache is a python modules base on local file for any python data struct",
    license = "MIT",
    url = "https://github.com/jamesqin-cn/tinycache",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
)