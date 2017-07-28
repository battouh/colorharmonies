# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='colorharmonies',
      version='1.0',
      description='Library to generate all your color harmonies with simplicity!',
      url='https://github.com/baptistemanteau/colorharmonies',
      author='Baptiste Manteau',
      author_email='manteau.baptiste@gmail.com',
      license='MIT',
      packages=['colorharmonies'],
      python_requires='>=3',
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)