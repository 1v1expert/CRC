#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='PCRC',
    version='0.1.1',
    description="Python CRC Calculations Modules",
    long_description=readme + '\n\n' + history,
    author="VLADDOS",
    author_email='1v1expert@gmail.com',
    url='https://github.com/1v1expert/CRC',
    packages=[
        'PCRC',
    ],
    package_dir={'PCRC':
                 'PCRC'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='PyCRC, CRC, CRC16, CRC16DNP, CRC16Kermit, CRC32',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)