"""Registries for looking up pre-defined game content.

The function *find_content* will find the class for a piece of content
when given the name of that content. For example:
``find_content("leather armor")`` will return the
*dungeonsheets.armor.LeatherArmor* class.

The *find_content* function is a shortcut that makes use of the
*default_content_registry*, which is a *ContentRegistry* instance that
is aware of all the content included in *dungeonsheets*. **New modules
should register themselves** with the *default_content_registry*, best
achieved by::

    from content_registry import default_content_registry
    default_content_registry.add_module(__name__)

In the case of **homebrew content**, the python file may not be in the
python path and so cannot be imported directly. In this case, the
*import_homebrew* function will import the python file-name given and
then register it with the *default_content_registry*, most often
within a character sheet file. For example, if the *PaperSword* weapon
class is defined in a separate file "my_homebrew.py", then in the
character file::

    from content_registry import import_homebrew
    import_homebrew("my_homebrew.py")
    
    weapons = ["paper sword"]

If homebrew content shares a name with canonical content, then lookup
by string will raise an exception. In those situations, the homebrew
content can be used directly from *import_homebrew*::

    from content_registry import import_homebrew
    campaign = import_homebrew("my_homebrew.py")
    
    weapons = [campaign.PaperSword]

"""


import sys
from pathlib import Path
from functools import lru_cache
import importlib.util
from typing import Union, List, Optional

from dungeonsheets import exceptions


class ContentRegistry:
    modules = None

    def __init__(self):
        self.modules = []

    def add_module(self, new_module):
        """Register a module with this registry.

        Adding the same module multiple times has no effect.

        *new_module* can also be a string, in which case, an attempt
        will be made to load the module from *sys.modules*. This way,
        a module can register itself::

            # Define classes, etc
            ...
            # Register the module
            registry = ContentRegistry()
            registry.add_module(__name__)
        
        """
        # Try and look up the module by name
        try:
            new_module = sys.modules[new_module]
        except KeyError:
            if isinstance(new_module, str):
                raise exceptions.ContentNotFound(f"Module could not be resolved: {repr(new_module)}")
        # Add the imported module to the list for later
        if new_module not in self.modules:
            self.modules.append(new_module)

    def findattr(self, name, valid_classes=[]):
        """Resolve the name of a piece of content to the corresponding Class.

        Similar to builtin getattr(obj, name) but more forgiving to
        whitespace and capitalization.

        valid_classes
          If given, only subclasses of classes in this list will be
          returned.

        """
        # Come up with several options
        try:
            name = name.strip()
        except AttributeError as e:
            # Probably not a string
            raise ValueError('content "%s" is not a valid identifier string.' % name)
        # check for +X weapons, armor, shields
        bonus = 0
        for i in range(1, 11):
            if (f"+{i}" in name) or (f"+ {i}" in name):
                bonus = i
                name = name.replace(f"+{i}", "").replace(f"+ {i}", "")
                break
        py_name = (
            name.replace("-", "_").replace(" ", "_").replace("'", "").replace("/", "")
        )
        camel_case = "".join([s.capitalize() for s in py_name.split("_")])
        # Check each module in the registry
        found_attrs = []
        for module in self.modules:
            if hasattr(module, py_name):
                # Direct lookup
                found_attrs.append(getattr(module, py_name))
            elif hasattr(module, camel_case):
                # CamelCase lookup
                found_attrs.append(getattr(module, camel_case))
        # Filter by valid classes
        if len(valid_classes) > 0:
            is_valid = [False for attr in found_attrs]
            for cls in valid_classes:
                is_valid = [
                    v
                    or isinstance(attr, cls)
                    or (isinstance(attr, type) and issubclass(attr, cls))
                    for v, attr in zip(is_valid, found_attrs)
                ]
            found_attrs = [attr for attr, v in zip(found_attrs, is_valid) if v]
        # Check that we found a valid, unique attribute
        if len(found_attrs) == 0:
            raise exceptions.ContentNotFound(f"Modules {self.modules} have no attribute {name}")
        elif len(found_attrs) > 1:
            raise exceptions.AmbiguousContent(f"Found multiple content entries for {name}")
        else:
            attr = found_attrs[0]
        # Apply weapon/etc. bonuses
        if bonus > 0:
            if (
                issubclass(attr, weapons.Weapon)
                or issubclass(attr, armor.Shield)
                or issubclass(attr, armor.Armor)
            ):
                attr = attr.improved_version(bonus)
        return attr


default_content_registry = ContentRegistry()


def find_content(name: str, valid_classes: Optional[List] = None):
    """Find content from a previously registered module.

    Parameters
    ==========
    name
      The name of the item to find. Can be "CamelCase", "under_case",
      or "lower case".
    valid_classes
      A list of parent classes to look for. If ``None`` or ``[]``, all
      classes will be considered valid.

    """
    if valid_classes is None:
        valid_classes = []
    return default_content_registry.findattr(name, valid_classes=valid_classes)


@lru_cache()
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
    default_content_registry.add_module(mod)
    return mod
