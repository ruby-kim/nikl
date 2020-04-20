#!/usr/bin/env python
from setuptools import setup, find_packages
import nikl


setup(name=nikl.__name__,
      description=nikl.__description__,
      version=nikl.__version__,
      author='Kyeongnam Kim',
      author_email='kkyy0126@naver.com',
      url=nikl.__url__,
      install_requires=nikl.__install_requires__,
      license=nikl.__license__,
      long_description=open('./README.md', 'r', encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      packages=find_packages(),
      classifiers=[
            "Development Status :: 4 - Beta,"
            "Programming Language :: Python :: 3",
            "License ::  MIT License",
            "National Language :: Korean",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX",
      ],
      python_requires='>=3.6',
      )
