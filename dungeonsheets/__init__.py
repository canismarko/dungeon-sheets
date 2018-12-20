from . import weapons, character, features, race, background, spells

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

__version__ = read('../VERSION')
