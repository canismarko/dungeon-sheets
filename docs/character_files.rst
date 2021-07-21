=================
 Character Files
=================

.. warning::

   Character files are python modules that are imported when
   parsed. **NEVER parse a character file without inspecting it** to
   verify that there are no unexpected consequences, especially a file
   from someone you do not trust.

Dungeonsheets expects one file per character, with a ``.py``
extension. This file is a python module, most likely with a series of
variables set describing the character. Any attribute beginning with
an underscore ('_') will be ignored. They are roughly grouped into
sections, which are documented below. Additionally, some
:ref:`examples<examples>` may be useful.

Each character file must contain a line like::

  dungeonsheets_version = "0.4.2"

Without this line, the :ref:`makesheets` command-line utility will ignore
the file. This is necessary to avoid importing non-D&D python files.

.. note::

   Some proficiencies, character traits, abilities, etc.\ are the
   result of the character's race and/or background. These **must
   still be included** in the character file and will not be
   automatically added if omitted.
   
Basic Info
==========

The character file will contain several basic information values that
are fairly self-evident. The values for ``character_class``,
``background``, ``race`` and ``alignment`` must match entries in the
standard 5e rules, and are case-insensitive. Refer to the D&D
`player's handbook`_ for more information.

.. code:: python
  
  name = 'Inara Serradon'
  character_class = 'wizard'
  player_name = 'Mark'
  background = "Acolyte"
  race = "High-Elf"
  level = 3
  alignment = "Chaotic good"
  xp = 2190
  hp_max = 16

Character Portrait
==================

.. code:: python

   portrait = True

If this is set to True and a corresponding portrait file exists,
the portrait will be added to the character personality sheet.
For now, the file must have a .jpeg extension and be named exactly
the same as the character file. This might not work with every Image size.
ca 550 * 700px seems to be the right format. Anything smaller should work, too.
See the Bard1 example for a demonstration of this feature.

Ability Scores
==============

Ability scores are numeric scores for each ability, as described in
the `player's handbook`_.

.. code:: python

   # Ability Scores
   strength = 10
   dexterity = 15
   constitution = 14
   intelligence = 16
   wisdom = 12
   charisma = 8

Proficiencies and Languages
===========================

This section may contain entries, one for ``skill_proficiencies`` and
one for ``languages``. ``skill_proficiencies`` must be an iterable of
case-insensitive strings matching skills described in the `player's
handbook`_. Languages is a standard string, since language proficiency
does not affect other areas of the character.

.. code:: python
   
   # Proficiencies and languages
   skill_proficiencies = [
       'arcana',
       'insight',
       'investigation',
       'perception',
       'religion',
   ]
   languages = "Common, Elvish, Draconic, Dwarvish, Goblin."


Inventory
=========

There are five entries for currencies, which must be
integers. ``weapons`` (iterable of strings), ``armor`` (string) and
``shield`` (string) must correspond to items available in the
`player's handbook`_. The ``equipment`` is a string that is rendered
as-is on the character sheet.

.. warning::

   Not all weapons and armor have been entered into the
   ``dungeonsheets`` library. If you receive an ``AttributeError``
   stating the item you entered is not defined despite being listed in
   the `player's handbook`_, please submit an `issue`_.

.. code:: python
   
   cp = 950
   sp = 75
   ep = 50
   gp = 120
   pp = 0
   weapons = ('shortsword', 'shortbow')
   armor = 'light leather armor'
   shield = 'shield'
   equipment = (
       """Shortsword, shortbow, 20 arrows, leather armor, thieves’ tools,
       backpack, bell, 5 candles, crowbar, hammer, 10 pitons, 50 feet of
       hempen rope, hooded lantern, 2 flasks of oil, 5 days rations,
       tinderbox, waterskin, crowbar, set of dark common clothes
       including a hood, pouch.""")

Spells
======

Two entries are available for spell-casting, and only if the class
supports spells. Both are lists of case-insensitive strings that must
correspond to spells described in the `player's handbook`_.

.. warning::

   Not all spells have been entered into the ``dungeonsheets``
   library. If you receive a ``UserWarning`` stating the spell you
   entered is not defined despite being listed in the `player's
   handbook`_, please submit an `issue`_.

.. code:: python

   # List of known spells
   spells = ('blindness deafness', 'burning hands', 'detect magic',
	     'false life', 'mage armor', 'mage hand', 'magic missile',
	     'prestidigitation', 'ray of frost', 'ray of sickness', 'shield',
	     'shocking grasp', 'sleep',)
   # Which spells have been prepared (not including cantrips)
   spells_prepared = ('blindness deafness', 'false life', 'mage armor',
	              'ray of sickness', 'shield', 'sleep',)

.. note::

   Some character classes have modified spellcasting mechanics that
   affects how these entries are intepreted.

   - `Druid`_



Personality and Backstory
=========================

This section contains string that describe the nature and backstory of
the character. They will be printed as-is on the character
sheet. Triple-quoted string and parenthesis may make the character's
source file more readable, but are not required.

.. code:: python
   
   # Backstory
   personality_traits = """I use polysyllabic words that convey the impression of
	                erudition. Also, I’ve spent so long in the temple that I have little
			experience dealing with people on a casual basis."""

   ideals = """Knowledge. The path to power and self-improvement is through
	    knowledge."""

   bonds = """The tome I carry with me is the record of my life’s work so far,
           and no vault is secure enough to keep it safe."""

   flaws = """I’ll do just about anything to uncover historical secrets that
           would add to my research."""

   features_and_traits = (
       """Spellcasting Ability: Intelligence is your spellcasting ability for
       your spells. The saving throw DC to resist a spell you cast is
       13. Your attack bonus when you make an attack with a spell is
       +5. See the rulebook for rules on casting your spells.
    
       Arcane Recovery: You can regain some of your magical energy by
       studying your spellbook. Once per day during a short rest, you can
       choose to recover expended spell slots with a combined level equal
       to or less than half your wizard level (rounded up).
    
       Darkvision: You see in dim light within a 60-foot radius of you as
       if it were bright light, and in darkness in that radius as if it
       were dim light. You can’t discern color in darkness, only shades
       of gray.
    
       Fey Ancestry: You have advantage on saving throws against being
       charmed, and magic can’t put you to sleep.
    
       Trance: Elves don’t need to sleep. They meditate deeply, remaining
       semiconscious, for 4 hours a day and gain the same benefit a human
       does from 8 hours of sleep.
    
       Shelter of the Faithful: As a servant of Oghma, you command the
       respect of those who share your faith, and you can perform the
       rites of Oghma. You and your companions can expect to receive free
       healing and care at a temple, shrine, or other established
       presence of Oghma’s faith. Those who share your religion will
       support you (and only you) at a modest lifestyle. You also have
       ties to the temple of Oghma in Neverwinter, where you have a
       residence. When you are in Neverwinter, you can call upon the
       priests there for assistance that won’t endanger them.""")


Class-Specific Features
=======================

Druid
-----

At level 2, druids choose a **circle**. This choice can affect
available wild_forms, and spellcasting abilities. The ``circle`` entry
should be set appropriately.

Druid's can transform into **wild shapes**, allowing them to adopt
some of the abilities of their new form. To aid in keeping track on
the possible shapes, Druids can have a listing for
``wild_shapes``. This list should contain names of beasts listed in
:py:mod:`dungeonsheets.monsters`, or instances of a subclass of
:py:class:`dungeonsheets.monsters.Monster`. If given, an extra *monster
sheet* will be produced as part of the PDF. Beasts familiar to the
druid but not yet accessible should still be listed to aid in record
keeping; they will be greyed-out on the sheet.

Additionally, druids don't learn spells, instead **druids can prepare
any spell available** provided it meets their level requirements. As
such, the listing for ``spells`` is not needed and **all prepared
spells and known cantrips** should be listed in the
``spells_prepared`` entry.

.. code:: python
   
   # We're a moon druid, why not
   circle = 'Moon'
	 
   # Spells are empty because we don't learn any spells
   spells = []
   # This one has all prepared spells and cantrips
   spells_prepared = ['druidcraft', 'cure wounds']

   # List of all the known wild shapes
   wild_shapes = ["wolf", "crocodile", 'ape', 'ankylosaurus']

Aftificer
---------

Artificers can specify known infusions. These will be rendered in a
similar manner to spells. They can be given in the ``infusions``
attribute of the character file:

.. code:: python

    infusions = ["enhanced_arcane_focus", "repulsion_shield"]

.. _player's handbook: http://dnd.wizards.com/products/tabletop-games/rpg-products/rpg_playershandbook

.. _issue: https://github.com/canismarko/dungeon-sheets/issues
