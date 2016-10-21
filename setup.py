import os
import sys
from setuptools import setup, find_packages, Extension, Command

setup(
    name='procslink',
    version='0.1.1',
    description='ProcsLink provides API for cross-namespace inter-process communication (IPC) over netlink socket.',
    license='MIT',
    author='Rayson Zhu',
    author_email='vfreex@gmail.com',
    url='https://github.com/vfreex/procslink',
    packages=find_packages(),
    long_description="This module is used for interprocess communication (IPC) for processes in difference namespaces."
                     "I designed and wrote this module because existing IPC libraries are not suitable for inter-namespaces communication."
                     "Currently, I have implemented a JSON-RPC interface.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX',
    ],
    keywords='ProcsLink IPC inter-process communication JSON-RPC',
)
