#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="dungeonsheets",
    version=read("VERSION"),
    description="Dungeons and Dragons 5e Character Tools",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    keywords="D&D character sheets",
    author="Mark Wolfman",
    author_email="canismarko@gmail.com",
    license="GPLv3",
    url="https://github.com/canismarko/dungeon-sheets",
    download_url="https://github.com/canismarko/dungeon-sheets/archive/master.zip",
    packages=find_packages(),
    package_data={
        "dungeonsheets": [
            "forms/*pdf",
            "forms/*.tex",
            "forms/*.txt",
            "modules/DND-5e-LaTeX-Template/*",
            "modules/DND-5e-LaTeX-Template/lib/*",
            "modules/DND-5e-LaTeX-Template/img/*",
            "../VERSION",
        ]
    },
    install_requires=[
        "fdfgen",
        "npyscreen",
        "jinja2",
        "pdfrw",
        "sphinx",
        "EbookLib",
        "reportlab",
    ],
    entry_points={
        "console_scripts": [
            "makesheets = dungeonsheets.make_sheets:main",
            "create-character = dungeonsheets.create_character:main",
        ]
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
)
