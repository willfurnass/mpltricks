from setuptools import setup, find_packages
import os 


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'mpltricks', # Y
    version = '0.0.1', # Y
    packages = find_packages(),

    install_requires = [
        "matplotlib >= 1.2.0",
    ],

    author = 'Will Furnass',
    author_email = 'will@thearete.co.uk',
    description='Helper functions for use with the matplotlib plotting library',
    license='GPL 3.0',
    keywords='matplotlib plotting',
)
