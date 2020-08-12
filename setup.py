#!/usr/bin/env python
#coding: utf-8

from setuptools import setup, find_packages

import airtable

setup(
    name="airtable",
    version=airtable.__version__,
    license=airtable.__license__,
    author=airtable.__author__,
    author_email="hello@romaincaraes.fr",
    description="A Python library for the Airtable API",
    long_description=open("README.md").read(),
    url="https://github.com/romaincaraes/airtable-python/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
    ],
)
