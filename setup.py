# Copyright (C) 2019 Atul Kadian
from setuptools import setup, find_packages

import gupload

long_desc = ""
try:
    import pypandoc
    long_desc = pypandoc.convert('README.md', 'rst', extra_args = ('--eol', 'lf'))
except(IOError, ImportError):
    long_desc = open('README.md').read()

setup(
    name = "gupload",
    version = "1.0",
    description = "A simple command line tool for uploading files to google drive and getting shared link",
    long_description = long_desc,
    classifiers = [
        "Development Status :: 1 - Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7"
    ],
    keywords = "Google Drive uploader",
    author = "Atul Kadian",
    author_email = "atul2143143@gmail.com",
    url = "https://github.com/AtulKadian/gupload",
    license = "GPL",
    packages = find_packages(),
    install_requires = [
        "google-api-python-client>=1.7.3",
        "google-auth>=1.5.0",
        "google-auth-httplib2<=0.0.3",
        "httplib2>=0.11.3",
        "oauth2client==4.1.3",
        "more-itertools>=4.2.0",
        "ndg-httpsclient>=0.4.0",
        "oauth>=1.0.1",
        "pyasn1>=0.4.3",
        "pyasn1-modules>=0.2.1",
        "uritemplate>=3.0.0",
        "urllib3>=1.23",
    ],
    python_requires = '2.7',
)
