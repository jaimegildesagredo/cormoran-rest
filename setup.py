#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import cormoran_rest

setup(
    name='cormoran_rest',
    version=cormoran_rest.__version__,
    description=cormoran_rest.__doc__,
    long_description=cormoran_rest.__doc__,
    author='Jaime Gil de Sagredo Luna',
    author_email='jaimegildesagredo@gmail.com',
    url='https://github.com/jaimegildesagredo/cormoran-rest',
    download_url='https://github.com/jaimegildesagredo/cormoran-rest/downloads',
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='tests',
    install_requires= [
        'cormoran',
        'tornado'
    ],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
