# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='betting event',
    version='0.1.8',
    description='Simple structure for handling events that you can be bet on',
    long_description=readme,
    author='Daniel Harris',
    author_email='dannyray44@hotmail.co.uk',
    url='https://github.com/dannyray44/betable_event',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'betting_event': ['defaults.json']}
)
