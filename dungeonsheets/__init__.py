__all__ = (
    "__version__",
    "Character",
    "weapons",
    "features",
    "mechanics",
    "race",
    "background",
    "spells",
    "import_homebrew",
)

from dungeonsheets import background, features, race, spells, weapons, mechanics
from dungeonsheets.character import Character
from dungeonsheets.content_registry import import_homebrew

import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


__version__ = read("../VERSION")
