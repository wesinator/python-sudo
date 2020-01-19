#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as license_file:
    license = license_file.read()

requirements = []

test_requirements = []

setup(
    name='sudo',
    version='0.1.0',
    description="""Module to run a subprocess command as another user, via sudo
    (not necessarily superuser/root)""",
    long_description=readme,
    author="wesinator",
    url='https://github.com/wesinator/python-sudo',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    zip_safe=True,
    keywords='sudo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
