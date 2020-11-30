from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks-markup',
    description='Hooks for pre-commit that validate Markdown / RST files',
    url='https://github.com/Lucas-C/pre-commit-hooks-markup',
    version='1.0.1',

    author='Lucas Cimon',
    author_email='lucas.cimon+pypi@gmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    install_requires=[
        'readme_renderer',
    ],
    entry_points={
        'console_scripts': [
            'rst_linter = pre_commit_hooks.rst_linter:main',
        ],
    },
)
