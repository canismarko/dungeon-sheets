===================
 Advanced Features
===================

.. warning::

   Character and GM files are python modules that are imported when
   parsed. **NEVER parse a character file without inspecting it** to
   verify that there are no unexpected consequences, especially a file
   from someone you do not trust.

Fancy Decorations (D&D 5e LaTeX Style)
======================================

Dungeonsheets can generate beautifully styled character sheets using the
official D&D 5e LaTeX template from `rpgtex/DND-5e-LaTeX-Template`_. This
makes your character sheets look like official Wizards of the Coast content
with proper formatting, colors, and decorations.

.. _rpgtex/DND-5e-LaTeX-Template: https://github.com/rpgtex/DND-5e-LaTeX-Template

Enabling Fancy Decorations
---------------------------

Use the ``--fancy`` (or ``-F``) flag when generating sheets:

.. code-block:: bash

   makesheets --fancy examples/wizard1.py
   # or short form
   makesheets -F examples/wizard1.py

What Gets Styled
----------------

When fancy decorations are enabled, the following pages receive D&D styling:

- **Spellbook pages**: Professional spell cards with proper formatting
- **Feature pages**: Class and racial features with D&D styling
- **Monster stat blocks**: Official-looking monster descriptions
- **Magic items**: Styled item descriptions
- **Druid wild shapes**: Creature stat blocks for wild form
- **Subclass features**: Beautifully formatted subclass abilities
- **Animal companions**: Companion creature stat blocks
- **Party summaries**: Styled party overview pages

Technical Details
-----------------

The D&D LaTeX template is included as a git submodule. When you clone the
repository, initialize it with:

.. code-block:: bash

   git clone https://github.com/canismarko/dungeon-sheets.git
   cd dungeon-sheets
   git submodule update --init --recursive

The template files are located in ``dungeonsheets/modules/DND-5e-LaTeX-Template/``.

.. note::

   Fancy decorations require LaTeX to be installed. The standard character
   sheet PDFs (without fancy decorations) use fillable PDF forms and don't
   require LaTeX.

How It Works
------------

When ``--fancy`` is used:

1. The LaTeX ``TEXINPUTS`` environment variable includes the DND template path
2. LaTeX runs **two passes** instead of one (for proper cross-references)
3. Jinja2 templates conditionally include ``\usepackage[layout=true]{dnd}``
4. Template files use conditional blocks based on ``use_dnd_decorations`` flag

The result is professional-looking output that matches the style of official
D&D 5e publications.

Comparison
----------

**Standard Mode** (``makesheets examples/wizard1.py``):

- Clean, functional fillable PDF forms
- Fast generation (no LaTeX required)
- Works without additional dependencies
- Best for quick reference and digital use

**Fancy Mode** (``makesheets --fancy examples/wizard1.py``):

- Beautiful D&D 5e styled output
- Looks like official WotC publications
- Requires LaTeX installation
- Best for printing and sharing

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


Magic Weapons and Armor
-----------------------

A common situation is the creation of homebrew weapons, armor and
shields. With multiple inheritance, it is possible to include such a
magic weapon as both a weapon and magic item:

.. code:: python

    from dungeonsheets import mechanics

    class DullSword(mechanics.Weapon, mechanics.MagicItem):
        """This magical sword does remarkably little damage."""
        name = "dull sword"
	# Weapon attributes, e.g.
	damage_bonus = -1
	attack_bonus = -1
	# Magical item attributes, e.g.
	item_type = "weapon"
	st_bonus_all = -1

    weapons = [DullSword]
    magic_items = [DullSword]

The same can be done by subclassing either ``mechanics.Armor`` or
``mechanics.Shield`` together with ``mechanics.MagicItem``.


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

