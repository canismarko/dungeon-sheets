#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='dungeonsheets',
      version=read('VERSION'),
      description='Dungeons and Dragons 5e Character Tools',
      long_description=read('README.rst'),
      long_description_content_type='text/x-rst',
      keywords='D&D character sheets',
      author='Mark Wolfman',
      author_email='canismarko@gmail.com',
      license='GPLv3',
      url='https://github.com/canismarko/dungeon-sheets',
      download_url = 'https://github.com/canismarko/dungeon-sheets/archive/master.zip',
      packages=['dungeonsheets'],
      package_data={
          'dungeonsheets': ['blank-character-sheet-default.pdf', 'blank-spell-sheet-default.pdf',
                            'spellbook_template.tex', 'druid_shapes_template.tex']
      },
      install_requires=[
          'fdfgen', 'npyscreen', 'jinja2', 'pdfrw',
      ],
      entry_points={
          'console_scripts': [
              'makesheets = dungeonsheets.make_sheets:main',
              'create-character = dungeonsheets.create_character:main',
          ]
      },
      python_requires='>=3.6',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Games/Entertainment :: Role-Playing',
      ],
     )
