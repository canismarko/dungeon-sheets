#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='dungeonsheets',
      version='0.1dev2',
      description='Dungeons and Dragons 5e Character Tools',
      author='Mark Wolfman',
      author_email='canismarko@gmail.com',
      url='https://github.com/canismarko/dungeon-sheets',
      download_url = 'https://github.com/canismarko/dungeon-sheets/archive/master.zip',
      packages=['dungeonsheets'],
      package_data={
          'dungeonsheets': ['blank-character-sheet-default.pdf', 'blank-spell-sheet-default.pdf']
      },
      install_requires=[
          'fdfgen',
      ],
      entry_points={
          'console_scripts': [
              'makesheets = dungeonsheets.make_sheets:main'
          ]
      },
     )
