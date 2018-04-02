================
 Dungeon Sheets
================

A tool to create character sheets for Dungeons and Dragons.

Installation
============

.. code:: bash

    $ pip install dungeonsheets

.. note::

   Dungeon sheets requires **at least python 3.6**. This is mostly due
   to the liberal use of f-strings_. If you want to use it with
   previous versions of python 3, you'll probably have to replace all
   the f-strings with the older ``.format()`` method or string
   interpolation.

.. _f-strings: https://www.python.org/dev/peps/pep-0498/

Usage
=====

Each character is described by a python file, which gives many
attributes associated with the character. See examples_ for more
information about the character descriptions.

.. _examples: https://github.com/canismarko/dungeon-sheets/tree/master/examples

The PDF's can then be generated using the ``makesheets`` command.

.. code:: bash

    $ cd examples
    $ makesheets

dungeon-sheets contains definitions for standard weapons and spells,
so attack bonuses and damage can be calculated automatically.
