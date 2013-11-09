#!/usr/bin/env python

from distutils.core import setup

setup(name='names',
      version='0.1',
      description='Random name and address generator',
      license='Apache 2',
      author='Francois Scharffe',
      author_email='francois.scharffe@lirmm.fr',
      url='http://github.com/lechatpito/Names',
      py_modules=['src/names/names'],
      packages=['names'],
      package_dir={'names': 'src/names'},
      package_data={'names': ['data/*.txt']},
     )
