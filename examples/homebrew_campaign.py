"""This file defines some homebrew mechanics that can be imported into
character sheets using ``dungeonsheets.import_homebrew``. See
``homebrew.py`` for an example of how these homebrew mechanics can be
used.

"""

from dungeonsheets import mechanics


class BrightSword(mechanics.Weapon):
    """Give you enemies the old razzle-dazzle."""
    name = "Brightsword"
