#!/usr/bin/env python

from distutils.core import setup

setup(name='dungeonsheets',
      version='0.1dev',
      description='Dungeons and Dragons 5e Character Tools',
      author='Mark Wolfman',
      author_email='canismarko@gmail.com',
      url='',
      packages=['dungeonsheets'],
      entry_points={
          'console_scripts': [
              'makesheets = dungeonsheets.make_sheets:main'
          ]
      },
     )
