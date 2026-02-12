#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banana语言安装配置文件
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='banana-language',
    version='0.1.0',
    description='Banana编程语言解释器',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Banana Language Team',
    author_email='banana@example.com',
    url='https://github.com/banana-language/banana',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[
        'ply',
        'lark-parser'
    ],
    entry_points={
        'console_scripts': [
            'banana=banana_interpreter_simple:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Interpreters',
    ],
    license='MIT',
    keywords='banana language interpreter programming',
)
