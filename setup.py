#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='windbird',
    version='0.1',
    description='A simple wind forecast twitter bot',
    author='Nils Werner',
    author_email='nils.werner@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests[security]',
        'ndg-httpsclient==0.3.0',  # otherwise tests will fail
        'tweepy',
        'pyyaml',
        'HTTPretty',
        'python-telegram-bot',
    ],
    extras_require={
        'docs': [
            'sphinx',
            'sphinxcontrib-napoleon',
            'sphinx_rtd_theme',
            'numpydoc',
        ],
        'tests': [
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'HTTPretty',
        ],
    },
    entry_points={
        'console_scripts': [
            'windbird = windbird:main',
        ]
    },
    classifiers=[
          'Development Status :: 2 - Beta',
          'Environment :: Console',
    ],
)
