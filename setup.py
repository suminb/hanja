#!/usr/bin/env python

from distutils.core import setup
import hanja

setup(name='hanja',
      py_modules=['hanja'],
      version=hanja.__version__,
      description='Hangul & Hanja library',
      author='Sumin Byeon',
      author_email='suminb@gmail.com',
      url='http://github.com/suminb/hanja',
      packages=[],
     )
