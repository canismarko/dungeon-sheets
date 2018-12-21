__all__ = ('__version__', 'Character', 'weapons', 'features',
           'character', 'race', 'background', 'spells')

from . import weapons, features, race, background, spells
from .character import Character

import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


__version__ = read('../VERSION')
