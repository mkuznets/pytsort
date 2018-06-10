# coding: utf-8
from setuptools import setup, find_packages


setup(
    name='pytsort',
    description='clone of tsort from GNU Coreutils',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pytsort = pytsort.main:main',
        ],
    },
)
