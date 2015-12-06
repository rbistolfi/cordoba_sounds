#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cba_sounds',
    version='1.0',
    description='Noise stats for Cordoba, Argentina',
    author='Rodrigo Bistolfi',
    author_email='rbistolfi@gmail.com',
    packages=['cba_sounds', 'cba_sounds.model', 'cba_sounds.views'],
)
