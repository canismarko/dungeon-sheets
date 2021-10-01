"""This file describes game-manager notes.

It's used for creating notes for the GM to keep track of various
monsters, etc.

"""

from dungeonsheets import mechanics


# This line (or one like it) is required in order for dungeonsheets to
# recognize the file.
dungeonsheets_version = "0.17.0"

# Specifying ``sheet_type = "gm"`` gives us GM notes instead of a
# player character sheet.
sheet_type = "gm"

# A short description of what happened last time, etc.
summary = """The party is about the enter the dungeon of *eternal tortuosity*."""

# A descriptive title to appear at the top of the document.
session_title = "Objects in Space - Session 1"

# Dungeonsheets supports a rudimentary version of cascading sheets. In
# this case, details for the whole campaign can be defined once, then
# sheets can be generated for each specific session using the
# *parent_sheets* attribute.
parent_sheets = ["gm-campaign-notes.py"]

# Defining a *monsters* attribute will include their stat blocks in
# the output
monsters = ["aboleth", "wolf", "giant eagle", "Vashta Nerada", "priest"]

# Arbitrary sections can be added to the GM notes. The
# ``extra_sections`` attribute should be a sequence of subclasses of
# the *Content* base class. For each entry in the sequence, the *name*
# attribute will be used for the section title, and the docstring will
# make up the body


class BBEGMotivation(mechanics.Content):
    """Hans Gruber is after the $640 in bearer bonds stored in *Nakatomi
    plaza*.

    """
    name = "Big-Bad-Evil-Guy Motivation"


class BarFight(mechanics.Content):
    """If the characters decide to go to the *Alliance Friendly Bar*,
    they will probably have to fight their way out against 5 enemies
    (3 Veteran, 2 Soldier).

    """
    name = "The Bar Fight"


extra_content = [BBEGMotivation, BarFight]
