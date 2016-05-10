from setuptools import setup, find_packages

setup(
    name='mpltricks',
    version='0.0.1',
    packages=find_packages(),

    install_requires=["matplotlib >= 1.2.0"],
    author='Will Furnass',
    author_email='will@thearete.co.uk',
    description='Helper functions for use with the matplotlib plotting library',
    license='GPL 3.0',
    keywords='matplotlib plotting',
)
