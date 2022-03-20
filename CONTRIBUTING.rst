===============================
 Contributing to Dungeonsheets
===============================

**Thanks for taking the time to contribute to dungeonsheets!**

Dungeonsheets is a small project and relies on volunteers like to you
to continue pushing new features and improvements. Issues and
pull-requests are welcomed and encouraged. This document is meant to
provide guidelines that clarify how you can best help; nothing is
written in stone.


Scope
=====

Dungeonsheets is intended as a tool for creating character sheets and
game-maker (GM/DM) sheets. A secondary goal is to provide high-level
classes that are suitable for incorporation to other projects.

Please ensure that all contributions are within the scope of
dungeonsheets, or if not, are accompanied by a compelling argument for
why the scope should be expanded. If your project requires changes to
a core class (e.g. ``Character``), these will be considered,
especially if the change will be broadly applicable to the usability
of that class.

What to Contribute
==================

Before submitting pull requests, please check the following:

- All tests in ``tests/`` pass.
- All example character sheets in the ``examples/`` directory build
  properly, both with and without the ``--fancy`` option.
- The submission passes linting by `flake8`_ (optional).
- The submission is formatted by `black`_ (optional).

.. _flake8: https://flake8.pycqa.org/en/latest/

.. _black: https://pypi.org/project/black/

Adding Features
---------------

Submissions for new features are welcome, provided they are within the
scope of dungeonsheets. **If the submission adds parameters to the
character.py schema**, please ensure the following:

- At least one example sheet (in ``examples/``) should include the
  new parameters, either by adding a new example or modifying an
  existing example.
- Older ``character.py`` sheets should still build properly without
  the parameter.
- Documentation in ``docs/`` is consistent with the new parameter.

Adding Content
--------------

Submissions with new game content (e.g. monsters, spells, features)
are welcome. The mechanics of the content should be included as a
**subclass of the relevant mechanic** (e.g. ``Monster``, ``Spell``,
``Feature``). The values themselves will be **attributes of this
subclass**. The description of the content should form the docstring
of the subclass. This docstring will be **rendered into the final
character sheet**, spellbook, etc. Therefore, is should be properly
formed `reStructuredText`_. Also, the docstring should be free of
extra content.

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Please **respect intellectual property rights** before submitting new
content. If you did not write the content that is being submitted,
check the relevant licensing to ensure there are no copyright or other
IP violations.


How to Contribute
=================

Running Tests
-------------

Dungeonsheets uses tests to verify the package works as
intended. Tests are found in the ``tests/`` folder. To run the tests
using *pytest*, run the following from a console:

.. code:: bash

	  pip install -r requirements.txt -r requirements-tests.txt
	  pytest

You can also run a sub-set of the tests, which can be convenient for
development. For example, to run just the tests related to dice
mechanics, use ``pytest tests/test_dice.py``. Dungeonsheets defines
tests using the *unittest* package in the standard library. **For
example**, to test a new function in the ``dungeonsheets/dice.py``
module, modify ``tests/test_dice.py``:

.. code-block:: python
   :caption: dice.py

   def roll(a, b=None):
       """roll(20) means roll 1d20, roll(2, 6) means roll 2d6"""
       if b is None:
           return random.randint(1, a)
       else:
           return sum([random.randint(1, b) for _ in range(a)])

.. code-block:: python
   :caption: test_dice.py

    from unittest import TestCase
    from dungeonsheets.dice import roll

    class TestDice(TestCase):
        def test_simple_rolling(self):
            num_tests = 100
            # Do a bunch of rolls and make sure the numbers are within the requsted range
            for _ in range(num_tests):
                result = roll(6)
                self.assertGreaterEqual(result, 1)
                self.assertLessEqual(result, 6)

        def test_multi_rolling(self):
            num_tests = 100
            for _ in range(num_tests):
                result = roll(2, 4)  # Roll 2d4
                self.assertGreaterEqual(result, 2)
                self.assertLessEqual(result, 8)


Building Documentation
----------------------

Dungeonsheets uses sphinx to build documentations. All files are in
reStructuredText and are kept in the ``docs/`` folder. To build the
HTML files, run:

.. code:: bash

	  pip install -r requirements.txt -r requirements-tests.txt
	  cd docs/
	  make html

The results can be found in the ``_build/html/`` foler.

Submitting Bugs
---------------

First, please check the list of `open issues`_ to make sure your bug
has no already been reported. If your bug has not been previously
reported, consider `submitting a new issue`_.

.. _open issues: https://github.com/canismarko/dungeon-sheets/issues

.. _submitting a new issue: https://github.com/canismarko/dungeon-sheets/issues/new

Submitting Pull Requests
------------------------

`Pull requests`_ are welcome, both for bug fixes and new features. At
a minimum, pull requests should not break existing tests.

.. _pull requests: https://github.com/canismarko/dungeon-sheets/pulls
