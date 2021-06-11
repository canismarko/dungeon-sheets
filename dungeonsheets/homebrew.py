"""Tools useful for defining homebrew content."""

from pathlib import Path
import importlib.util
from typing import Union


def import_homebrew(filepath: Union[str, Path]):
    """Import a module file containing homebrew content.

    This is intended to be used in a character/GM sheet to load in
    homebrew content defined in an external file.

    Parameters
    ==========
    filepath
      The location of the python file containing the homebrew content.
    
    Returns
    =======
    mod
      The imported module of homebrew content.

    """
    spec = importlib.util.spec_from_file_location("module.name", filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
