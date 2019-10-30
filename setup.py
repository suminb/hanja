#!/usr/bin/env python

from distutils.core import setup
import hanja


def readme():
    try:
        with open("README.rst") as f:
            return f.read()
    except:
        return "(Could not read from README.rst)"


setup(
    name="hanja",
    py_modules=["hanja/__init__", "hanja.hangul"],
    version=hanja.__version__,
    description="Hangul & Hanja library",
    long_description=readme(),
    author=hanja.__author__,
    author_email=hanja.__email__,
    url="https://github.com/suminb/hanja",
    packages=["hanja"],
    package_data={"hanja": ["table.yml"]},
    include_package_data=True,
)
