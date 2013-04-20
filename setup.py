#!/usr/bin/env python

from distutils.core import setup
import hanja

setup(name='hanja',
      py_modules=['hanja', 'hanja.pairs'],
      version=hanja.__version__,
      description='Hangul & Hanja library',
      author=hanja.__author__,
      author_email=hanja.__email__,
      url='http://github.com/suminb/hanja',
      packages=[],
     )
