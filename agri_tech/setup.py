#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Stella Kibika",
    author_email='steshykibika@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Loading and using Lidar data",
    entry_points={
        'console_scripts': [
            'agri_tech=agri_tech.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='agri_tech',
    name='agri_tech',
    packages=find_packages(include=['agri_tech', 'agri_tech.*']),
    package_data={'': ['filename.txt']},
    include_package_data=True,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Kibika/Lidar-Data-Pipeline/agri_tech',
    version='0.1.0',
    zip_safe=False,
)
