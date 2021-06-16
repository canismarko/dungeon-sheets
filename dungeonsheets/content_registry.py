from pathlib import Path
from functools import lru_cache
import importlib.util
from typing import Union, List, Optional

from dungeonsheets import (
    weapons,
    monsters,
    race,
    background,
    armor,
    spells,
    infusions,
    magic_items,
    features,
)


class ContentRegistry:
    modules = None

    def __init__(self):
        self.modules = []

    def add_module(self, new_module):
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
        name = name.strip()
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
            raise AttributeError(f"Modules {self.modules} have no attribute {name}")
        elif len(found_attrs) > 1:
            raise RuntimeError(f"Found multiple content entries for {name}")
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
default_content_registry.add_module(weapons)
default_content_registry.add_module(monsters)
default_content_registry.add_module(race)
default_content_registry.add_module(background)
default_content_registry.add_module(armor)
default_content_registry.add_module(spells)
default_content_registry.add_module(infusions)
default_content_registry.add_module(magic_items)
default_content_registry.add_module(features)


def find_content(name: str, valid_classes: Optional[List]):
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
