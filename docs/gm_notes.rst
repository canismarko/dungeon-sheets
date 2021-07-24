==========
 GM Notes
==========

.. warning::

   GM notes files are python modules that are imported when
   parsed. **NEVER parse a gm notes file without inspecting it** to
   verify that there are no unexpected consequences, especially a file
   from someone you do not trust.

Dungeonsheets has the ability to parse a python file with entities
needed for game manager (GM) session notes.

Each file must contain a line like::

  dungeonsheets_version = "0.4.2"
  sheet_type = "gm"

Without the version line, the ``makesheets`` command-line utility
will ignore the file. This is necessary to avoid importing non-D&D
python files. Without the ``sheet_type`` line, the file will be
interpreted as a character sheet.

Basic Info
==========

Currently, these attributes are supported: ``monsters`` and
``session_title``. More attributes will be added in the future, but if
there's something specific you have a need for, please consider
`contributing`_ an issue or pull-request.

.. code:: python
  
   session_title = "Objects in Space"
   monsters = ["ogre", "giant eagle"]
   party = ["rogue1.py", "paladin2.py"]

``monsters`` should be a list of either strings or subclasses of
:py:class:`Monster`. These entries will then by listed on the
resulting PDF with their stat block and features.

``party`` contains a list of filenames for the characters in the
party. These will produce a summary table of the attributes of your
party.

.. _contributing: https://github.com/canismarko/dungeon-sheets/blob/master/CONTRIBUTING.rst

Random Tables
=============

Random tables can be used in-game to make decisions on-the-fly. These
tables can be included in the PDF using ``random_tables``. Currently
the following random tables are available.

- **"conjure animals"** - A list of options to choose from when a
  player casts the *Conjure Animals* spell.

.. code-block:: python
   :caption: Example:	  
   
   random_tables = ["conjure animals"]	 

Adding Arbitrary Content
========================

Additional content can be included in arbitrary sections that get
added to the end of the GM notes output. In addition to the attributes
described above, suitable extra attributes in the notes (``.py``) file
will be rendered as a new section, with a heading based on the name of
the attribute and a body with the content parsed as restructured
text. Attributes that begin with an underscore ("_") or those that are
not a string will be ignored.

For example, the following entry will be rendered as a new section
with the heading "The Bar Fight":

.. code-block:: python

    the_bar_fight = (
         "If the characters decide to go to the *Alliance Friendly Bar*, "
	 "they will probably have to fight their way out against 5 enemies "
	 "(3 Veteran, 2 Soldier)."
    )
