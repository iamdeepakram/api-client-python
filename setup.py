# coding: utf-8

"""
    Flat API

    OpenAPI spec version: 2.0.0
    Contact: developers@flat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "flat_api"
VERSION = "0.5.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

try:
    import pypandoc
    LONG_DESCRIPTION = open('README.md').read()
    LONG_DESCRIPTION = LONG_DESCRIPTION[:LONG_DESCRIPTION.index('## Documentation for API Endpoints')]
    LONG_DESCRIPTION = pypandoc.convert_text(LONG_DESCRIPTION, 'rst', format='md')
except(IOError, ImportError):
    LONG_DESCRIPTION = open('README.md').read()

setup(
    name=NAME,
    version=VERSION,
    description="Flat API Client",
    author="The Flat Team (https://flat.io)",
    author_email="developers@flat.io",
    url="https://github.com/FlatIO/api-client-python",
    keywords=["Flat API", "MusicXML", "Music Notation", "MIDI"],
    long_description=LONG_DESCRIPTION,
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    license="Apache",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Artistic Software",
        "Topic :: Education",
        "Topic :: Multimedia :: Sound/Audio"
    ]
)
