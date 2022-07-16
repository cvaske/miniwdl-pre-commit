#!/usr/bin/env python3

from setuptools import setup

setup(
    name="miniwdl-pre-commit",
    version="v1.6.0",
    description="Pre-commit plugin for miniwdl",
    url="https://github.com/cvaske/miniwdl-pre-commit.git",
    author="Charles Vaske",
    author_email="cvaske@gmail.com",
    license="MIT",
    install_requires=["miniwdl==1.6.0"],
    packages=["miniwdl-pre-commit"],
    zip_safe=False,
)
