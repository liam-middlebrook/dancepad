#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="DancePad-Keyboard",
    version=version,
    description=("A project using the Arduino that allows users to simulate "
        "keyboard inputs via a dancepad."),
    classifiers=[],
    keywords="arduino physical dance game",
    author="Liam Middlebrook",
    author_email="liammiddlebrook@gmail.com",
    url="https://github.com/liam-middlebrook/dancepad-keyboard",
    license="MIT License",
    packages=find_packages(
    ),
    scripts=[
        "distribute_setup.py",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "PySerial",
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)