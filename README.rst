================
 Dungeon Sheets
================

A tool to create character sheets for Dungeons and Dragons.

Installation
============

.. code:: bash

    $ pip install dungeonsheets

Usage
=====

Each character is described by a python file, which gives many
attributes associated with the character. See examples_ for more
information about the character descriptions.

.. _examples: 

The PDF's can then be generated using the ``makesheets`` command.

.. code:: bash

    $ cd examples
    $ makesheets

dungeon-sheets contains definitions for standard weapons and spells,
so attack bonuses and damage can be calculated automatically.
