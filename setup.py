#! /usr/bin/env python3
# Copyright (C) 2019 Heuna Kim (heynaheyna9@gmail.com)
# Licensed under the MIT license

import os

from setuptools import find_packages, setup

_description = ('Django management commands to visualize migration graphs')

_project_url = 'https://github.com/hahey/django-migration-vis'


def _get_long_description():
    readme_rst = os.path.join(os.path.dirname(__file__), 'README.rst')
    with open(readme_rst) as f:
        return f.read()


if __name__ == '__main__':
    setup(
        name='django-migration-vis',
        url=_project_url,
        description=_description,
        long_description=_get_long_description(),
        license='MIT',
        version='2.0.0',
        author='Heuna Kim',
        author_email='heynaheyna9@gmail.com',
        packages=find_packages(exclude=('example', 'example.*')),
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        install_requires=[
            'Django>=2.2',
            'graphviz',
        ],
        python_requires='>=3.7',
    )
