"""Standard setup script for the py_common_subseq.

@author: A. Samuel Pottinger (samnsparky, Gleap LLC, https://gleap.org)
@license: MIT
"""

import os

from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='py_common_subseq',
    version='0.1.1',
    packages=['py_common_subseq'],
    author='A. Samuel Pottinger',
    url='https://github.com/Samnsparky/py_common_subseq',
    description=('Micro-library finding all common subsequences between two ',
        'sequences in polynomial time.'),
    license='MIT',
    keywords='all common subsequences ACS dynamic programming',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing'
    ],
    download_url='https://github.com/Samnsparky/py_common_subseq/archive/master.zip'
)