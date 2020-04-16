#!/usr/bin/env python
from setuptools import setup, find_packages
import nikl


setup(name=nikl.__name__,
      description=nikl.__description__,
      version=nikl.__version__,
      author='Kyeongnam Kim',
      author_email='kkyy0126@naver.com',
      url=nikl.__url__,
      #download_url=nikl.__download_url__,
      install_requires=nikl.__install_requires__,
      license=nikl.__license__,
      long_description=open('./README.md', 'r', encoding='utf-8').read(),
      packages=find_packages(),
      classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
      ]
      )
