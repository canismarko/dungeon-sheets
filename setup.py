#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup

setup(name='dungeonsheets',
      version='0.1dev1',
      description='Dungeons and Dragons 5e Character Tools',
      author='Mark Wolfman',
      author_email='canismarko@gmail.com',
      url='https://github.com/canismarko/dungeon-sheets',
      download_url = 'https://github.com/canismarko/dungeon-sheets/archive/master.zip',
      packages=['dungeonsheets'],
      entry_points={
          'console_scripts': [
              'makesheets = dungeonsheets.make_sheets:main'
          ]
      },
     )
