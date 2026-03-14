===============
 Dungeon Sheets
===============

A tool to create character sheets and session notes for Dungeons and
Dragons 5th edition (D&D 5e).

.. image:: https://github.com/stiffneckjim/dungeon-sheets/actions/workflows/docker.yml/badge.svg
   :target: https://github.com/stiffneckjim/dungeon-sheets/actions/workflows/docker.yml
   :alt: Docker Build Status

.. image:: https://github.com/stiffneckjim/dungeon-sheets/actions/workflows/python-ci.yml/badge.svg
   :target: https://github.com/stiffneckjim/dungeon-sheets/actions/workflows/python-ci.yml
   :alt: Python CI Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

Documentation
=============

Documentation can be found on readthedocs_.

.. _readthedocs: https://dungeon-sheets.readthedocs.io/en/latest/?badge=latest


Docker
======

You can run this repository directly from a container. The container images are automatically 
built and published to GitHub Container Registry (GHCR) using GitHub Actions workflows.

Available Tags
--------------

- ``master``: Latest development version from the master branch
- ``latest``: Latest stable release
- Specific version tags (e.g. ``v0.19.0``)

Running the Container
---------------------

Run the following in a directory with valid character files (such as the examples_ directory):

.. code:: bash

    $ docker run -it -v $(pwd):/build ghcr.io/stiffneckjim/dungeon-sheets:master

Building Locally
----------------

To build the container locally:

.. code:: bash

    $ docker build -t dungeon-sheets .

Running Tests with Docker
-------------------------

You can build and run the dedicated test image stage to execute the full test suite
inside the containerized environment.

Build the test stage:

.. code:: bash

    $ docker build --target dungeon-sheets-test -t dungeon-sheets-test .

Run the test stage image:

.. code:: bash

    $ docker run --rm -it dungeon-sheets-test

The test image runs ``.devcontainer/run-tests.sh``, which executes the project's
test checks in the container.

Container Details
-----------------

The container:

- Is based on Ubuntu with required dependencies (pdftk, texlive) pre-installed
- Mounts the current directory as ``/build`` to access character files
- Includes the latest version of dungeon-sheets from the specified branch/tag

Windows Usage
-------------

**Prerequisites:**

- Docker Desktop for Windows installed and running (https://www.docker.com/products/docker-desktop/)
- Character files ready (Python ``.py`` files or JSON exports from VTTs)

**Quick Start:**

1. Build the image (one-time setup):

   .. code:: powershell

       cd C:\path\to\dungeon-sheets
       docker build -t dungeon-sheets .

2. Or use the pre-built image (faster, no build needed):

   .. code:: powershell

       docker pull ghcr.io/stiffneckjim/dungeon-sheets:main

**Generate Character Sheets:**

Using PowerShell:

.. code:: powershell

    # Navigate to your character files directory
    cd C:\DnD\Characters

    # Generate fancy sheets with decorations
    docker run -it -v ${PWD}:/build ghcr.io/stiffneckjim/dungeon-sheets:main --fancy

    # Generate all sheets recursively
    docker run -it -v ${PWD}:/build ghcr.io/stiffneckjim/dungeon-sheets:main --fancy --recursive

    # Generate editable PDF forms
    docker run -it -v ${PWD}:/build ghcr.io/stiffneckjim/dungeon-sheets:main --editable

Using Command Prompt (CMD):

.. code:: cmd

    cd C:\DnD\Characters
    docker run -it -v %cd%:/build ghcr.io/stiffneckjim/dungeon-sheets:main --fancy

**Common Options:**

- ``--fancy``: Generate sheets with D&D styling and decorations (recommended!)
- ``--editable``: Create fillable PDF forms
- ``--recursive``: Process all character files in subdirectories
- ``--output-format=epub``: Generate ePub format for tablets/e-readers

**Example Workflow:**

.. code:: powershell

    # One-time: Create folder and pull image
    mkdir C:\DnD\MyGroup
    docker pull ghcr.io/stiffneckjim/dungeon-sheets:main

    # Add your character .py or .json files to C:\DnD\MyGroup

    # Generate sheets before each session
    cd C:\DnD\MyGroup
    docker run -it -v ${PWD}:/build ghcr.io/stiffneckjim/dungeon-sheets:main --fancy --recursive

The PDFs will be created in the same folder, ready to print or share!

**Troubleshooting:**

- Make sure Docker Desktop is running (check system tray for whale icon)
- Enable file sharing in Docker Desktop → Settings → Resources → File Sharing
- Use ``--debug`` flag for detailed error messages


Installation
============

.. code:: bash

    $ pip install dungeonsheets

For Development
---------------

If you want to contribute or use the fancy D&D 5e LaTeX styling, clone with submodules:

.. code:: bash

    $ git clone https://github.com/canismarko/dungeon-sheets.git
    $ cd dungeon-sheets
    $ git submodule update --init --recursive
    $ pip install -e ".[dev]"

The submodule includes the `D&D 5e LaTeX template`_ for beautiful character sheets.

.. _D&D 5e LaTeX template: https://github.com/rpgtex/DND-5e-LaTeX-Template

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
a fallback python library (pypdf) will be used. This has the
limitation that it is not able to flatten PDF forms.

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

.. _examples: https://github.com/stiffneckjim/dungeon-sheets/tree/master/examples

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

By default, your character's spells are ordered alphabetically. If you
would like your spellbook to be ordered by level, you can use the ``-S``
option to do so.

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
    the same plane of existence as you. The target must make a Wisdom
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

For content that is not part of the SRD, consider using other
sources. As an example, parse5e_ can be used to retrieve spells.


.. _parse5e: https://github.com/user18130814200115-2/parse5e
