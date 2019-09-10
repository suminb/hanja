import os

import yaml


basepath = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(basepath, 'table.json')

with open(filename) as fin:
    table = yaml.load(fin.read())
