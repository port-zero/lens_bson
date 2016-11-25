#!/usr/bin/env python
import os
from setuptools import setup, find_packages

longdescr = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.md'
    )
).read()


setup(
    name='lens_bson',
    author='Veit Heller',
    version='0.0.1',
    license='MIT',
    url='https://github.com/port-zero/lens_bson',
    description='A BSON parser for lens',
    long_description=longdescr,
    packages=find_packages('.'),
    install_requires=[
        "pygments",
        "lens",
        "bson",
    ],
)

