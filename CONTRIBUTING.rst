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
  properly.
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
