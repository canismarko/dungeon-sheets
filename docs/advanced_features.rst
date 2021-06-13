===================
 Advanced Features
===================

.. warning::

   Character and GM files are python modules that are imported when
   parsed. **NEVER parse a character file without inspecting it** to
   verify that there are no unexpected consequences, especially a file
   from someone you do not trust.

Homebrew
========

Dungeonsheets provides mechanisms for including items and abilities
outside of the standard rules ("homebrew"). This can be done in one of
two ways.

1. As subclasses (recommended)
2. As strings

Subclasses (Recommended)
------------------------

The best option is to define your homebrew item directly in the
character file as a subclass of one of the basic mechanics:

- :py:class:`dungeonsheets.spells.Spell`
- :py:class:`dungeonsheets.features.Feature`
- :py:class:`dungeonsheets.infusions.Infusion`
- :py:class:`dungeonsheets.weapons.Weapon`
- :py:class:`dungeonsheets.armor.Armor`
- :py:class:`dungeonsheets.armor.Shield`
- :py:class:`dungeonsheets.magic_items.MagicItem`

For convenience, these are all available in the
:py:mod:`dungeonsheets.mechanics` module. With this approach, a
homebrew weapon can be specified in the character file. See the
relevant super class for relevant attributes.

.. code:: python

    from dungeonsheets import mechanics

    class DullSword(mechanics.Weapon):
	  """Bonk things with it."""
          name = "Dullsword"
	  base_damage = "10d6"

    weapons = ['shortsword', DullSword]

These homebrew definitions can also be stored in a separate file
(e.g. *my_homebrew.py*), then imported and used in multiple character
files:

.. code:: python

    from dungeonsheets import import_homebrew
    
    
    my_homebrew = import_homebrew("my_campaign.py")

    weapons = ["shortsword", my_homebrew.DullSword]

The :py:func:`import_homebrew` function also registers the module with
the global content manager, so in the above example ``weapons =
[my_homebrew.DullSword]`` and ``weapons = ["dull sword"]`` are
equivalent. See the :ref:`homebrew example` example for more examples.

Strings
-------

If a mechanic is listed in a character file, but not built into
dungeonsheets, it will still be listed on the character sheet with
generic attributes. This should be viewed as a fallback to the
recommended subclass method above, so that attributes and descriptions
can be given.

    
Roll20 (VTTES) and Foundry JSON Files
=====================================

Dungeonsheets has partial support for reading JSON files exported
either from roll20.net using the `VTTES browser extension`_, or
directly from `Foundry VTT`_ by choosing *export data* from the
actor's right-click menu. This allows character sheets to be exported
from roll20.net and foundry, and then rendered into full character
sheets.

.. _VTTES browser extension: https://wiki.5e.tools/index.php/R20es_Install_Guide

.. _Foundry VTT: https://foundryvtt.com/article/actors/


Cascading Sheets
================

Character and GM sheet files can **inherit from other character and GM
files**. This has two primary use cases:

1. A parent GM sheet can be made for a campaign, and then child sheets
   can provide only the specific details needed for each session.
2. When importing JSON files from roll20 or Foundry VTT, missing
   features (e.g. Druid wild shapes) can be added manually.

Sheet cascading is activated by using the ``parent_sheets`` attribute
in a python sheet file, which should be a list of paths to other
sheets (either ``.py`` or ``.json``):



.. code-block:: python
   :caption: gm_session1_notes.py
    
    dungeonsheets_version = "0.15.0"
    monsters = ['giant eagle', 'wolf', 'goblin']
    parent_sheets = ['gm_generic_notes.py']


.. code-block:: python
   :caption: gm_generic_notes.py
    
    dungeonsheets_version = "0.15.0"
    party = ["rogue1.py", "paladin2.py", ...]

