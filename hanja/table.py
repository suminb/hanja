import os
import yaml


def load_table(filename):
    """Loads the Hanja table."""
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import BaseLoader as Loader
    with open(filename) as fin:
        table = yaml.load(fin.read(), Loader=Loader)

    return table


basepath = os.path.abspath(os.path.dirname(__file__))
hanja_table = load_table(os.path.join(basepath, "table.yml"))
