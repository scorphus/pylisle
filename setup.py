#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Lisle
# https://github.com/scorphus/pylisle

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2018, Pablo S. Blum de Aguiar <scorphus@gmail.com>

import os

from setuptools import find_packages, setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


tests_require = [
    'autopep8',
    'flake8',
    'ipdb',
    'isort',
    'pytest-cov',
    'sphinx',
    'tox',
]

setup(
    name='lisle',
    version='0.1.0',
    url='http://pypi.python.org/pypi/lisle',
    license='MIT',
    description=(
        'Lisle (Link Station Locator) helps you find the best link station '
        'based on its reach and distance from a given device.'
    ),
    long_description=read('README.md'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Problem Solving',
    ],
    keywords='link station locator reach power distance',
    author='Pablo S. Blum de Aguiar',
    author_email='scorphus@gmail.com',
    packages=find_packages(),
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'tests': tests_require,
    },
    include_package_data=True,
    zip_safe=False,
)
