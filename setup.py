#!/usr/bin/env python

from distutils.core import setup
import hanja


def readme():
    try:
        f = open('README.rst')
        content = f.read()
        f.close()
        return content
    except IOError:
        pass
    except OSError:
        pass


setup(name='hanja',
      py_modules=['hanja', 'hanja.pairs'],
      version=hanja.__version__,
      description='Hangul & Hanja library',
      long_description=readme(),
      author=hanja.__author__,
      author_email=hanja.__email__,
      url='http://github.com/suminb/hanja',
      packages=[],
     )
