#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []
test_requirements = []

setup(
    name='sudo',
    version='1.0.0',
    description="Modular Python to execute any subprocess commands as another user "\
    "(not necessarily superuser/root)",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="wesinator",
    url='https://github.com/wesinator/python-sudo',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    zip_safe=True,
    keywords='sudo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
