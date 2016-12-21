# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample_python_package',
    version='0.0.3',
    description='Sample package for Python',
    long_description=readme,
    author='John Doe',
    author_email='john@doe.com',
    url='https://github.com/avihoo/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

