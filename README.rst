================
 Dungeon Sheets
================

A tool to create character sheets and session notes for Dungeons and
Dragons 5th edition (D&D 5e).

.. image:: https://travis-ci.com/canismarko/dungeon-sheets.svg?branch=master
   :target: https://travis-ci.com/canismarko/dungeon-sheets
   :alt: Build status

.. image:: https://coveralls.io/repos/github/canismarko/dungeon-sheets/badge.svg
   :target: https://coveralls.io/github/canismarko/dungeon-sheets
   :alt: Test coverage status

.. image:: https://readthedocs.org/projects/dungeon-sheets/badge/?version=latest
   :target: https://dungeon-sheets.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

Documentation
=============

Documentation can be found on readthedocs_.

.. _readthedocs: https://dungeon-sheets.readthedocs.io/en/latest/?badge=latest

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

Optional External dependencies
==============================

* You may use **pdftk** to generate the sheets in PDF format.
* You will need **pdflatex**, and a few latex packages, installed to
  generate the PDF spell pages (optional).

If **pdftk** is available, it will be used for pdf generation. If not,
a fallback python library (pdfrw) will be used. This has some
limitations:

- Produces v1.3 PDF files
- Not able to flatten PDF forms
- Will produce separate character-sheets, spell-lists and spell-books.
  
Different linux distributions have different names for packages. While
pdftk is available in Debian and derivatives as **pdftk**, the package
is not available in some RPM distributions, such as Fedora and CentOS.
One alternative would be to build your PC sheets using docker.

If the ``pdflatex`` command is available on your system, spellcasters
will include a spellbook with descriptions of each spell known. If
not, then this feature will be skipped.

In order to properly format descriptions for spells/features/etc.,
some additional latex packages are needed. On Ubuntu these can be
install with:

.. code:: bash

    $ sudo apt-get -y install pdftk texlive-latex-base texlive-latex-extra texlive-fonts-recommended

Usage
=====

Each character or set of GM notes is described by a python (or a VTTES
JSON) file, which gives many attributes associated with the
character. See examples_ for more information about the character
descriptions.

.. _examples: https://github.com/canismarko/dungeon-sheets/tree/master/examples

The PDF's can then be generated using the ``makesheets`` command. If
no filename is given, the current directory will be parsed and any
valid files found will be processed. If the ``--recursive`` option is
used, sub-folders will also be parsed.

.. code:: bash

    $ cd examples
    $ makesheets

dungeon-sheets contains definitions for standard weapons and spells,
so attack bonuses and damage can be calculated automatically.

Consider using the ``-F`` option to include the excellent D&D 5e
template for rendering spellbooks, druid wild forms and features
pages (https://github.com/rpgtex/DND-5e-LaTeX-Template).

If you'd like a **step-by-step walkthrough** for creating a new
character, just run ``create-character`` from a command line and a
helpful menu system will take care of the basics for you.


Content Descriptions
====================

The descriptions of content elements (e.g. classes, spells, etc.) are
included in docstrings. The descriptions should ideally conform to
reStructured text. This allows certain formatting elements to be
properly parsed and rendered into LaTeX or HTML::

  class Scrying(Spell):
    """You can see and hear a particular creature you choose that is on
    the same plane of existence as you. The target must make a W isdom
    saving throw, which is modified by how well you know the target
    and the sort of physical connection you have to it. If a target
    knows you're casting this spell, it can fail the saving throw
    voluntarily if it wants to be observed.

    Knowledge - Save Modifier
    -------------------------
    - Secondhand (you have heard of the target) - +5
    - Firsthand (you have met the target) - +0
    - Familiar (you know the target well) - -5

    Connection - Save Modifier
    --------------------------
    - Likeness or picture - -2
    - Possession or garment - -4
    - Body part, lock of hair, bit of nail, or the like - -10

    """
    name = "Scrying"
    level = 5
    ...
