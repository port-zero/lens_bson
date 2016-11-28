#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='lens_bson',
    author='Veit Heller',
    version='0.0.2',
    license='MIT',
    url='https://github.com/port-zero/lens_bson',
    download_url = 'https://github.com/port-zero/lens_bson/tarball/0.0.2',
    description='A BSON parser for lens',
    packages=find_packages('.'),
    install_requires=[
        "pygments",
        "lens-cli",
        "bson",
    ],
)

