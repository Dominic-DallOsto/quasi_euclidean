from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='quasi-euclidean',
    version='0.0.1',
    description='Python implementation of R\'s quasieuclid function.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['quasieuclid', 'distance', 'matrix'],
    url='https://github.com/Dominic-DallOsto/quasi_euclidean',
    author='Dominic Dall\'Osto',
    author_email='dominicd7@hotmail.com',
    license='GPLv3',
    packages=find_packages(),
    install_requires=['numpy', 'scipy'],
    )