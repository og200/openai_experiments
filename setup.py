#!/usr/bin/env python
import os

from setuptools import setup, find_packages
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    return paths


f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

setup(
    name='openai_experiments',
    version='0.0.1',
    description='Sketches for OpenAI experimentation',
    long_description=long_description,
    author='Flow Innovation',
    author_email='info@flow-innovation.com',
    url='http://www.github.io/og200/openai_experiments/',
    packages=find_packages(),
    package_data={
        '': [],
    },
    install_requires=[
        'openai'
    ]
)