#!/usr/bin/env python

from setuptools import setup, find_packages
from pkg_resources import parse_requirements

import hanja


def readme():
    try:
        with open("README.rst") as f:
            return f.read()
    except:
        return "(Could not read from README.rst)"


with open("requirements.txt") as f:
    install_requires = [str(x) for x in parse_requirements(f.read())]

setup(
    name="hanja",
    version=hanja.__version__,
    description="Hangul & Hanja library",
    long_description=readme(),
    author=hanja.__author__,
    author_email=hanja.__email__,
    url="https://github.com/suminb/hanja",
    packages=find_packages(include=["hanja", "hanja.*"]),
    package_data={"": ["requirements.txt"], "hanja": ["table.yml"]},
    include_package_data=True,
    install_requires=install_requires,
)
