#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkgversion import list_requirements, pep440_version
from setuptools import setup, find_packages

setup(
    name='py-pkgversion',
    version=pep440_version(),
    description="Versioning utils for python projects",
    long_description=open('README.md').read(),
    author="Niels Lensink",
    author_email='niels@elements.nl',
    url='https://stash.kpnnl.local/DE/py-pkgversion',
    install_requires=list_requirements('requirements/requirements-base.txt'),
    packages=find_packages(exclude=['pkgversion.tests*']),
    tests_require=['tox'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
