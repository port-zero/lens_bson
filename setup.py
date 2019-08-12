#!/usr/bin/env python
import os
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='lens_bson',
    author='Veit Heller',
    version='0.0.3',
    license='MIT',
    url='https://github.com/port-zero/lens_bson',
    download_url = 'https://github.com/port-zero/lens_bson/tarball/0.0.3',
    description='A BSON parser for lens',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages('.'),
    install_requires=[
        "pygments",
        "lens-cli",
        "bson",
    ],
)

