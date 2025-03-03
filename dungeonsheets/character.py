"""Tools for describing a player character."""
from __future__ import annotations  # To support python 3.10 annotation in older version
import logging
import math
import os
import re
import warnings
from pathlib import Path
from types import ModuleType
from typing import Sequence, Union, MutableMapping

import jinja2

from dungeonsheets import (
    armor,
    background,
    classes,
    exceptions,
    features,
    infusions,
    magic_items,
    monsters,
    race,
    spells,
    weapons,
)
from dungeonsheets.content import Creature
from dungeonsheets.content_registry import find_content
from dungeonsheets.dice import combine_dice
from dungeonsheets.equipment_reader import equipment_weight_parser
from dungeonsheets.weapons import Weapon

log = logging.getLogger(__name__)

dice_re = re.compile(r"(\d+)d(\d+)")

__all__ = (
    "Artificer",
    "Barbarian",
    "Bard",
    "Cleric",
    "Character",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard",
)

multiclass_spellslots_by_level = {
    # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
    1: (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    2: (0, 3, 0, 0, 0, 0, 0, 0, 0, 0),
    3: (0, 4, 2, 0, 0, 0, 0, 0, 0, 0),
    4: (0, 4, 3, 0, 0, 0, 0, 0, 0, 0),
    5: (0, 4, 3, 2, 0, 0, 0, 0, 0, 0),
    6: (0, 4, 3, 3, 0, 0, 0, 0, 0, 0),
    7: (0, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    8: (0, 4, 3, 3, 2, 0, 0, 0, 0, 0),
    9: (0, 4, 3, 3, 3, 1, 0, 0, 0, 0),
    10: (0, 4, 3, 3, 3, 2, 0, 0, 0, 0),
    11: (0, 4, 3, 3, 3, 2, 1, 0, 0, 0),
    12: (0, 4, 3, 3, 3, 2, 1, 0, 0, 0),
    13: (0, 4, 3, 3, 3, 2, 1, 1, 0, 0),
    14: (0, 4, 3, 3, 3, 2, 1, 1, 0, 0),
    15: (0, 4, 3, 3, 3, 2, 1, 1, 1, 0),
    16: (0, 4, 3, 3, 3, 2, 1, 1, 1, 0),
    17: (0, 4, 3, 3, 3, 2, 1, 1, 1, 1),
    18: (0, 4, 3, 3, 3, 3, 1, 1, 1, 1),
    19: (0, 4, 3, 3, 3, 3, 2, 1, 1, 1),
    20: (0, 4, 3, 3, 3, 3, 2, 2, 1, 1),
}


class Character(Creature):
    """A generic player character."""

    # Character-specific
    name = "Unknown Hero"
    player_name = ""
    xp = 0
    # Extra hit points info, for characters only
    hp_current = None
    hp_temp = 0
    hit_dice_current = ""
    # Base stats (ability scores)
    inspiration = False
    attacks_and_spellcasting = ""
    class_list = list()
    _background = None
    _companions = []
    _carrying_capacity = 0
    _carrying_weight = 0
    equipment_weight_dict = {}

    # Characteristics
    personality_traits = (
        "TODO: Describe how your character behaves, interacts with others"
    )
    ideals = "TODO: Describe what values your character believes in."
    bonds = "TODO: Describe your character's commitments or ongoing quests."
    flaws = "TODO: Describe your character's interesting flaws."
    features_and_traits = "Describe any other features and abilities."
    chosen_tools = ""

    _proficiencies_text = list()

    # Appearance
    portrait: Path | None = None  # Path to image file
    symbol: Path | None = None  # Path to image file
    # List of custom images:
    # [(path_to_image_file, page_index,
    # x_center_coordinate, y_center_coordinate,
    # max_width, max_height)]
    images: list[tuple[Path, int, int, int, int, int]] = []

    source_file_location: Path | None

    age = 0
    height = ""
    weight = ""
    eyes = ""
    skin = ""
    hair = ""
    # Background
    allies = ""
    faction_name = ""
    # faction_symbol = placeholder not sure how to implement
    backstory = ""
    additional_description = ""
    other_feats_traits = ""
    treasure = ""
    org_name = ""

    def __init__(
        self,
        classes: Sequence = [],
        levels: Sequence[int] = [],
        subclasses: Sequence = [],
        **attrs,
    ):
        """Create a new character from attributes *attrs*.

        **Multiclassing** can be accomplished by a list of class names
        *classes*, and a list of class levels *levels*.

        Parameters
        ==========
        classes
          Strings with class names, or character class definitions
          representing the characters various D&D classes.
        levels
          The class levels for each corresponding class entry in
          *classes*.
        subclasses
          Subclasses that apply for this character.
        **attrs
          Additional keyword parameters to set as attributes for this
          character.

        """
        super(Character, self).__init__()
        self.clear()
        # make sure class, race, background are set first
        my_classes = classes
        my_levels = levels
        my_subclasses = subclasses
        # backwards compatability
        if len(my_classes) == 0:
            if "class" in attrs:
                my_classes = [attrs.pop("class")]
                my_levels = [attrs.pop("level", 1)]
                my_subclasses = [attrs.pop("subclass", None)]
            else:  # if no classes or levels given, default to Lvl 1 Fighter
                my_classes = ["Fighter"]
                my_levels = [1]
                my_subclasses = [None]
        # Generate the list of class objects
        self.add_classes(
            my_classes,
            my_levels,
            my_subclasses,
            feature_choices=attrs.get("feature_choices", []),
        )
        # parse race and background
        self.race = attrs.pop("race", None)
        self.background = attrs.pop("background", None)
        # parse images
        self.symbol = attrs.pop("symbol", None)
        self.images = attrs.pop("images", [])
        if self.symbol:
            self.images = [(self.symbol, 1, 492, 564, 145, 113)] + self.images
        self.portrait = attrs.pop("portrait", None)
        if self.portrait:
            self.images = [(self.portrait, 1, 117, 551, 170, 220)] + self.images
        self.source_file_location = attrs.pop("source_file_location", None)
        self.images = [
            (
                Path(path),
                page_index,
                x_center_coordinate,
                y_center_coordinate,
                max_width,
                max_height,
            )
            if Path(path).is_absolute()
            else (
                Path(self.source_file_location) / path,
                page_index,
                x_center_coordinate,
                y_center_coordinate,
                max_width,
                max_height,
            )
            for path, page_index, x_center_coordinate, y_center_coordinate, max_width, max_height in self.images
        ]
        # parse all other attributes
        self.set_attrs(**attrs)
        self.__set_max_hp(attrs.get("hp_max", None))

    def clear(self):
        # reset class-defined items
        self.class_list = list()
        self._weapons = list()
        self.magic_items = list()
        self._saving_throw_proficiencies = tuple()
        self.other_weapon_proficiencies = tuple()
        self.skill_proficiencies = list()
        self.skill_expertise = list()
        self._proficiencies_text = list()
        self._spells = list()
        self._spells_prepared = list()
        self.infusions = list()
        self.custom_features = list()
        self.feature_choices = list()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.class_name}: {self.name}>"

    def add_class(
        self,
        cls: (classes.CharClass, type, str),
        level: (int, str),
        subclass=None,
        feature_choices: Sequence = [],
    ):
        """Add a class, level, and subclass the character has attained."""
        if isinstance(cls, str):
            cls = cls.strip().title().replace(" ", "")
            try:
                cls = getattr(classes, cls)
            except AttributeError:
                raise AttributeError(
                    "class was not recognized from classes.py: {:s}".format(cls)
                )
        if isinstance(level, str):
            level = int(level)
        self.class_list.append(
            cls(level, owner=self, subclass=subclass, feature_choices=feature_choices)
        )

    def add_classes(
        self,
        classes_list: Sequence[Union[str, classes.CharClass]] = [],
        levels: Sequence[Union[int, float, str]] = [],
        subclasses: Sequence = [],
        feature_choices: Sequence = [],
    ):
        """Add several classes, levels, etc.

        The lists can also be single values for a single class
        character.

        """
        if isinstance(classes_list, str):
            classes_list = [classes_list]
        if (
            isinstance(levels, int)
            or isinstance(levels, float)
            or isinstance(levels, str)
        ):
            levels = [levels]
        if len(levels) == 0:
            levels = [1] * len(classes_list)
        if isinstance(subclasses, str):
            subclasses = [subclasses]
        if len(subclasses) < len(classes_list):
            for count in range(0, (len(classes_list) - len(subclasses))):
                subclasses.append(None)
        assert len(classes_list) == len(
            levels
        ), "the length of classes {:d} does not match length of levels {:d}".format(
            len(classes), len(levels)
        )
        assert len(classes_list) == len(
            subclasses
        ), "the length of classes {:d} does not match length of subclasses {:d}".format(
            len(classes_list), len(subclasses)
        )
        for cls, lvl, sub in zip(classes_list, levels, subclasses):
            params = {}
            params["feature_choices"] = feature_choices
            self.add_class(cls=cls, level=lvl, subclass=sub, **params)

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, newrace):
        if isinstance(newrace, race.Race):
            self._race = newrace
            self._race.owner = self
        elif isinstance(newrace, type) and issubclass(newrace, race.Race):
            self._race = newrace(owner=self)
        elif isinstance(newrace, str):
            try:
                self._race = find_content(newrace, valid_classes=[race.Race])(
                    owner=self
                )
            except exceptions.ContentNotFound:
                msg = f'Race "{newrace}" not defined. Please add it to ``race.py``'
                self._race = race.Race(owner=self)
                warnings.warn(msg)
        elif newrace is None:
            self._race = race.Race(owner=self)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, bg):
        if isinstance(bg, background.Background):
            self._background = bg
            self._background.owner = self
        elif isinstance(bg, type) and issubclass(bg, background.Background):
            self._background = bg(owner=self)
        elif isinstance(bg, str):
            try:
                self._background = find_content(
                    bg, valid_classes=[background.Background]
                )(owner=self)
            except exceptions.ContentNotFound:
                msg = (
                    f'Background "{bg}" not defined. Please add it to ``background.py``'
                )
                self._background = background.Background(owner=self)
                warnings.warn(msg)

    @property
    def class_name(self):
        if self.num_classes >= 1:
            return self.primary_class.name
        else:
            return ""

    @property
    def classes_and_levels(self):
        return " / ".join([f"{c.name} {c.level}" for c in self.class_list])

    @property
    def class_names(self):
        return [c.name for c in self.class_list]

    @property
    def levels(self):
        return [c.level for c in self.class_list]

    @property
    def subclasses(self):
        return [c.subclass for c in self.class_list if c.subclass is not None]

    @property
    def level(self):
        return sum(c.level for c in self.class_list)

    @level.setter
    def level(self, new_level):
        self.primary_class.level = new_level
        if self.num_classes > 1:
            warnings.warn(
                "Unable to tell which level to set. Updating "
                "level of primary class {:s}".format(self.primary_class.name)
            )

    @property
    def num_classes(self):
        return len(self.class_list)

    @property
    def has_class(self):
        return self.num_classes > 0

    @property
    def primary_class(self):
        # for now, assume first class given must be primary class
        if self.has_class:
            return self.class_list[0]
        else:
            return None

    def __set_max_hp(self, hp_max):
        """
        Set maximum HP based on value in charlist py or calc from classes
        """
        if hp_max:
            assert isinstance(hp_max, int), hp_max.__class__
            self.hp_max = hp_max
        else:
            const_mod = self.constitution.modifier
            level_one_hp = self.primary_class.hit_dice_faces + const_mod
            self.hp_max = level_one_hp
            for char_cls in self.class_list:
                hp_per_lvl = char_cls.hit_dice_faces / 2 + 1 + const_mod
                levels = char_cls.level
                if char_cls == self.primary_class:
                    levels -= 1
                assert levels >= 0
                self.hp_max += int(hp_per_lvl * levels)

    @property
    def weapon_proficiencies(self):
        wp = set(self.other_weapon_proficiencies)
        wp |= {weapons.Unarmed}  # Everyone is proficient in unarmed strikes
        if self.num_classes > 0:
            wp |= set(self.primary_class.weapon_proficiencies)
        if self.num_classes > 1:
            for c in self.class_list[1:]:
                wp |= set(c.multiclass_weapon_proficiencies)
        if self.race is not None:
            wp |= set(getattr(self.race, "weapon_proficiencies", ()))
        if self.background is not None:
            wp |= set(getattr(self.background, "weapon_proficiencies", ()))
        return tuple(wp)

    @weapon_proficiencies.setter
    def weapon_proficiencies(self, new_weapons):
        self.other_weapon_proficiencies = tuple(new_weapons)

    @property
    def other_weapon_proficiencies_text(self):
        return tuple(w.name for w in self.other_weapon_proficiencies)

    @property
    def features(self):
        fts = set(self.custom_features)
        fighting_style_defined = False
        set_of_fighting_styles = {
            "Fighting Style (Archery)",
            "Fighting Style (Defense)",
            "Fighting Style (Dueling)",
            "Fighting Style (Great Weapon Fighting)",
            "Fighting Style (Protection)",
            "Fighting Style (Two-Weapon Fighting)",
        }
        for temp_feature in fts:
            fighting_style_defined = temp_feature.name in set_of_fighting_styles
            if fighting_style_defined:
                break

        if not self.has_class:
            return fts
        for c in self.class_list:
            fts |= set(c.features)
            for feature in fts:
                if (
                    fighting_style_defined
                    and feature.name == "Fighting Style (Select One)"
                ):
                    temp_feature = feature
                    fts.remove(temp_feature)
                    break
        if self.race is not None:
            fts |= set(getattr(self.race, "features", ()))
            # some races have level-based features (Ex: Aasimar)
            if hasattr(self.race, "features_by_level"):
                for lvl in range(1, self.level + 1):
                    fts |= set(self.race.features_by_level[lvl])
        if self.background is not None:
            fts |= set(getattr(self.background, "features", ()))

        return sorted(tuple(fts), key=(lambda x: x.name))

    @property
    def features_by_type(self):
        if not self.has_class:
            return set(self.custom_features)
        fts = list()
        character_feat_choices = list()
        other_feat_choices = list()
        # Add player choices; distinguish between general feats and
        # feat choices such as fighting styles and metamagic options.
        for item in self.custom_features:
            if item.source == "Feats":
                character_feat_choices.append(item)
            else:
                other_feat_choices.append(item)
        for c in self.class_list:
            for item in list(c.features):
                # Treat features that are instances of other features the
                # same as feature choices, so that we can sort them later.
                # Example: Blood Curse of Corrosion.
                # Parent class:             cls.__class__.__bases__[0]
                if (not (item.__class__.__bases__[0] == features.Feature
                        or type(item) == features.Feature)
                        and item.__class__.__bases__[0] in c.features):
                    other_feat_choices.append(item)
            for item in list(c.features):
                if not item in other_feat_choices:
                    fts.append(item)
                # Now check whether any items in class_feat_choices
                # is a subclass of current item.
                for choice in other_feat_choices:
                    if choice.__class__.__bases__[0] == item.__class__:
                        fts.append(choice)
            # Make sure we didn't miss any feat choices:
            for choice in other_feat_choices:
                if not choice in fts:
                    fts.insert(0, choice)
        if self.race is not None:
            for item in getattr(self.race, "features", ()):
                fts.append(item)
            # some races have level-based features (Ex: Aasimar)
            if hasattr(self.race, "features_by_level"):
                for lvl in range(1, self.level + 1):
                    for item in list(self.race.features_by_level[lvl]):
                        fts.append(item)
        if self.background is not None:
            for item in getattr(self.background, "features", ()):
                fts.append(item)
        return tuple(character_feat_choices + fts)

    @property
    def custom_features_text(self):
        return tuple([f.name for f in self.custom_features])

    def has_feature(self, feat):
        return any([isinstance(f, feat) for f in self.features])

    @property
    def saving_throw_proficiencies(self):
        if self.primary_class is None:
            return self._saving_throw_proficiencies
        else:
            return (
                self._saving_throw_proficiencies
                or self.primary_class.saving_throw_proficiencies
            )

    @saving_throw_proficiencies.setter
    def saving_throw_proficiencies(self, vals):
        self._saving_throw_proficiencies = vals

    @property
    def spellcasting_classes(self):
        return [c for c in self.class_list if c.is_spellcaster]

    @property
    def spellcasting_classes_excluding_warlock(self):
        return [c for c in self.spellcasting_classes if c is not classes.Warlock]

    @property
    def is_spellcaster(self):
        return len(self.spellcasting_classes) > 0

    def spell_slots(self, spell_level):
        warlock_slots = 0
        for c in self.spellcasting_classes:
            if type(c) is classes.Warlock:
                warlock_slots = c.spell_slots(spell_level)
        if len(self.spellcasting_classes_excluding_warlock) == 0:
            return warlock_slots
        if len(self.spellcasting_classes_excluding_warlock) == 1:
            return (
                self.spellcasting_classes_excluding_warlock[0].spell_slots(spell_level)
                + warlock_slots
            )
        else:
            if spell_level == 0:
                return sum([c.spell_slots(0) for c in self.spellcasting_classes])
            else:
                # compute effective level from PHB pg 164
                eff_level = 0
                for c in self.spellcasting_classes_excluding_warlock:
                    if type(c) in [
                        classes.Bard,
                        classes.Cleric,
                        classes.Druid,
                        classes.Sorcerer,
                        classes.Wizard,
                    ]:
                        eff_level += c.level
                    elif type(c) in [classes.Paladin, classes.Ranger]:
                        eff_level += c.level // 2
                    elif type(c) in [classes.Fighter, classes.Rogue]:
                        eff_level += c.level // 3
                    elif type(c) is classes.Artificer:
                        eff_level += math.ceil(c.level / 2)
                if eff_level == 0:
                    return warlock_slots
                else:
                    return (
                        multiclass_spellslots_by_level[eff_level][spell_level]
                        + warlock_slots
                    )

    @property
    def spells(self):
        spells = set(self._spells) | set(self._spells_prepared)
        for f in self.features:
            spells |= set(f.spells_known) | set(f.spells_prepared)
        for c in self.spellcasting_classes:
            spells |= set(c.spells_known) | set(c.spells_prepared)
        return sorted(tuple(spells), key=(lambda x: x.name))

    @property
    def spells_prepared(self):
        spells = set(self._spells_prepared)
        for f in self.features:
            spells |= set(f.spells_prepared)
        for c in self.spellcasting_classes:
            spells |= set(c.spells_prepared)
        return sorted(tuple(spells), key=(lambda x: x.name))

    def set_attrs(self, **attrs):
        """
        Bulk setting of attributes
        Useful for loading a character from a dictionary
        """
        for attr, val in attrs.items():
            if attr == "dungeonsheets_version":
                pass  # Maybe we'll verify this later?
            elif attr == "character_file_location":
                pass
            elif attr == "weapons":
                if isinstance(val, str):
                    val = [val]
                # Treat weapons specially
                for weap in val:
                    self.wield_weapon(weap)
            elif attr == "magic_items":
                if isinstance(val, str):
                    val = [val]
                for mitem in val:
                    msg = (
                        f'Magic Item "{mitem}" not defined. '
                        "Please add it to ``magic_items.py``"
                    )
                    ThisMagicItem = self._resolve_mechanic(
                        mechanic=mitem,
                        SuperClass=magic_items.MagicItem,
                        warning_message=msg,
                    )
                    self.magic_items.append(ThisMagicItem(wielder=self))
            elif attr == "weapon_proficiencies":
                self.other_weapon_proficiencies = ()
                msg = 'Magic Item "{}" not defined. Please add it to ``weapons.py``'
                wps = set(
                    [
                        self._resolve_mechanic(
                            w, SuperClass=weapons.Weapon, warning_message=msg
                        )
                        for w in val
                    ]
                )
                wps -= set(self.weapon_proficiencies)
                self.other_weapon_proficiencies = list(wps)
            elif attr == "armor":
                self.wear_armor(val)
            elif attr == "shield":
                self.wield_shield(val)
            elif attr == "circle":
                if hasattr(self, "Druid"):
                    self.Druid.circle = val
            elif attr == "features":
                if isinstance(val, str):
                    val = [val]
                _features = []
                for f in val:
                    msg = 'Feature "{}" not defined. Please add it to ``features.py``'
                    ThisFeature = self._resolve_mechanic(
                        mechanic=f,
                        SuperClass=features.Feature,
                        warning_message=msg,
                    )
                    _features.append(ThisFeature)
                self.custom_features += tuple(F(owner=self) for F in _features)
            elif (attr == "spells") or (attr == "spells_prepared"):
                # Create a list of actual spell objects
                _spells = []
                for spell_name in val:
                    msg = 'Spell "{}" not defined. Please add it to ``spells.py``'
                    ThisSpell = self._resolve_mechanic(
                        mechanic=spell_name,
                        SuperClass=spells.Spell,
                        warning_message=msg,
                    )
                    _spells.append(ThisSpell)
                # Sort by name
                _spells.sort(key=lambda spell: spell.name)
                # Save list of spells to character atribute
                if attr == "spells":
                    # Instantiate them all for the spells list
                    self._spells = tuple(S() for S in _spells)
                else:
                    # Instantiate them all for the spells list
                    self._spells_prepared = tuple(S() for S in _spells)
            elif attr == "infusions":
                if hasattr(self, "Artificer"):
                    _infusions = []
                    for infusion_name in val:
                        msg = (
                            "Infusion '{}' not defined. Please add it to"
                            " ``infusions.py``"
                        )
                        ThisInfusion = self._resolve_mechanic(
                            mechanic=infusion_name,
                            SuperClass=infusions.Infusion,
                            warning_message=msg,
                        )
                        _infusions.append(ThisInfusion)
                    _infusions.sort(key=lambda infusion: infusion.name)
                    self.infusions = tuple(i() for i in _infusions)
            elif type(val) not in (type, ModuleType):
                # Some other generic attribute
                is_unknown = not hasattr(self, attr) and not attr.startswith("_")
                if is_unknown:
                    warnings.warn(
                        f"Setting unknown character attribute {attr}", RuntimeWarning
                    )
                # Lookup general attributes
                setattr(self, attr, val)

    def spell_save_dc(self, class_type):
        ability_mod = getattr(self, class_type.spellcasting_ability).modifier
        return 8 + self.proficiency_bonus + ability_mod

    def spell_attack_bonus(self, class_type):
        ability_mod = getattr(self, class_type.spellcasting_ability).modifier
        return self.proficiency_bonus + ability_mod

    def is_proficient(self, weapon: Weapon):
        """Is the character proficient with this item?

        Considers class proficiencies and race proficiencies.

        Parameters
        ----------
        weapon
          The weapon to be tested for proficiency.

        Returns
        -------
        Boolean: is this character proficient with this weapon?

        """
        all_proficiencies = self.weapon_proficiencies
        is_proficient = any((isinstance(weapon, W) for W in all_proficiencies))
        return is_proficient

    @property
    def proficiencies_text(self):
        final_text = ""
        all_proficiencies = tuple(self._proficiencies_text)
        if self.has_class:
            all_proficiencies += tuple(self.primary_class._proficiencies_text)
        if self.num_classes > 1:
            for c in self.class_list[1:]:
                all_proficiencies += tuple(c._multiclass_proficiencies_text)
        if self.race is not None:
            all_proficiencies += tuple(self.race.proficiencies_text)
        if self.background is not None:
            all_proficiencies += tuple(self.background.proficiencies_text)
        # Create a single string out of all the proficiencies
        for txt in all_proficiencies:
            if not final_text:
                # Capitalize the first entry
                txt = txt.capitalize()
            else:
                # Put a comma first
                txt = ", " + txt
                # Add this item to the list text
            final_text += txt
        # Add a period at the end
        final_text += "."
        return final_text

    @proficiencies_text.setter
    def proficiencies_text(self, val):
        try:
            profs = val.split(",")
        except AttributeError:
            profs = val
        self._proficiencies_text = profs
        if self.chosen_tools == "":
            self.chosen_tools = ", ".join(item for item in profs)

    @property
    def features_text(self):
        s = "\n\n--".join(
            [f.name + ("**" if f.needs_implementation else "") for f in self.features]
        )
        if s != "":
            s = "(See Features Page)\n\n--" + s
            s += "\n\n=================\n\n"
        return s

    @property
    def features_summary(self):
        # save space for informed features and traits
        if hasattr(self, "features_and_traits"):
            info_list = []
            N = 30
            if re.search(r'\S',  self.features_and_traits):
                info_list = ["**Other Features**"]
                info_list += [
                    text.strip()
                    for text in self.features_and_traits.split("\n\n")
                    if not (text.isspace())
                ]
                N = len(info_list)
                for text in info_list:
                    if len(text) > 26:  # 26 is just a guess for expected size of lines
                        N += 1
                if N > 30:
                    return "\n".join(info_list[:30]) + "\n(...)"
                N = 30 - N
        if len(self.class_list) > 1:
            featS = ["**Multiclass**:"]
            for cl in self.class_list:
                description = cl.name
                if cl.subclass:
                    description += f"/{cl.subclass}"
                description += f" {cl.level}"
                featS.append(description)
        else:
            featS = []
        featS += ["**Features**"]
        featS += [f.name for f in self.features]
        if len(featS) > N:
            featS = featS[:N] + ["(...)"]
        featS += info_list
        return "\n\n".join(featS)

    @property
    def carrying_capacity(self):
        _ccModD = {
            "tiny": 0.5,
            "small": 1,
            "medium": 1,
            "large": 2,
            "huge": 4,
            "gargantum": 8,
        }
        cc_mod = _ccModD[self.race.size.lower()]
        return 15 * self.strength.value * cc_mod

    @property
    def carrying_weight(self):
        weight = equipment_weight_parser(self.equipment, self.equipment_weight_dict)
        weight += sum([w.weight for w in self.weapons])
        if self.armor:
            weight += self.armor.weight
        if self.shield:
            weight += 6
        weight += sum([self.cp, self.sp, self.ep, self.gp, self.pp]) / 50
        return round(weight)

    @property
    def equipment_text(self):
        eq_list = []
        if hasattr(self, "equipment") and len(self.equipment.strip()) > 0:
            eq_list += [
                text.strip()
                for text in self.equipment.split("\n\n")
                if not (text.isspace())
            ]
        if hasattr(self, "magic_items") and len(self.magic_items) > 0:
            sub_list = "**Magic Items:** "
            for item in self.magic_items:
                sub_list += item.name + ", "
            eq_list += [sub_list[:-2]]
        return "\n\n".join(eq_list)

    @property
    def weight_and_capacity_text(self):
        cw, cc = self.carrying_weight, self.carrying_capacity
        return f"**Weight:** {cw} lb **Capacity:** {cc} lb"

    @property
    def proficiencies_by_type(self):
        prof_dict = {}
        w_pro = set(self.weapon_proficiencies)
        w_pro.remove(weapons.Unarmed)
        if weapons.MartialWeapon in w_pro:
            prof_dict["Weapons"] = ["All Weapons"]
        elif weapons.SimpleWeapon in w_pro:
            prof_dict["Weapons"] = ["Simple Weapons"]
            for w in w_pro:
                if not (issubclass(w, weapons.SimpleWeapon)):
                    prof_dict["Weapons"] += [w.name]
        else:
            prof_dict["Weapons"] = [w.name for w in w_pro]
        if "Weapons" in prof_dict.keys():
            prof_dict["Weapons"] = ", ".join(prof_dict["Weapons"])
        armor_types = ["all armor", "light armor", "medium armor", "heavy armor"]
        prof_set = set(
            [
                prof.lower().strip().strip(".")
                for prof in self.proficiencies_text.split(",")
            ]
        )
        prof_dict["Armor"] = [ar.title() for ar in armor_types if ar in prof_set]
        if len(prof_dict["Armor"]) > 2 or 'all armor' in prof_set:
            prof_dict["Armor"] = ["All Armor"]
        if 'shields' in prof_set:
            prof_dict["Armor"] += ["Shields"]
        prof_dict["Armor"] = ", ".join(prof_dict["Armor"])
        if hasattr(self, 'chosen_tools'):
            prof_dict["Other"] = re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                                       lambda word: word.group(0).capitalize(),
                                       self.chosen_tools)
        return prof_dict

    @property
    def spell_casting_info(self):
        """Returns a ready-to-use dictionary for spellsheets."""
        level_names = [
            "Cantrip",
            "FirstLevelSpell",
            "SecondLevelSpell",
            "ThirdLevelSpell",
            "FourthLevelSpell",
            "FifthLevelSpell",
            "SixthLevelSpell",
            "SeventhLevelSpell",
            "EighthLevelSpell",
            "NinthLevelSpell",
        ]
        spell_info = {
            "head": {
                "classes_and_levels": " / ".join(
                    [c.name + " " + str(c.level) for c in self.spellcasting_classes]
                ),
                "abilities": " / ".join(
                    [
                        c.spellcasting_ability.upper()[:3]
                        for c in self.spellcasting_classes
                    ]
                ),
                "DCs": " / ".join(
                    [str(self.spell_save_dc(c)) for c in self.spellcasting_classes]
                ),
                "bonuses": " / ".join(
                    [
                        "{:+d}".format(self.spell_attack_bonus(c))
                        for c in self.spellcasting_classes
                    ]
                ),
            }
        }
        slots = {
            level_names[k]: self.spell_slots(k)
            for k in range(1, 10)
            if self.spell_slots(k) > 0
        }
        spell_info["slots"] = slots
        spell_list = {}
        for s in self.spells:
            prepared = s in self.spells_prepared
            level_info = level_names[s.level]
            info_there = spell_list.get(level_info, [])
            spell_list[level_info] = info_there + [(s.name, prepared)]
        spell_info["list"] = spell_list
        return spell_info

    @property
    def magic_items_text(self):
        s = ", ".join(
            [f.name for f in sorted(self.magic_items, key=(lambda x: x.name))]
        )
        if s:
            s += ", "
        return s

    def wear_armor(self, new_armor):
        """Accepts a string or Armor class and replaces the current armor.

        If a string is given, then a subclass of
        :py:class:`~dungeonsheets.armor.Armor` is retrived from the
        ``armor.py`` file. Otherwise, an subclass of
        :py:class:`~dungeonsheets.armor.Armor` can be provided
        directly.

        """
        if new_armor not in ("", "None", None):
            if isinstance(new_armor, armor.Armor):
                new_armor = new_armor
            else:
                msg = 'Unnown armor "{}". Please add it to ``armor.py``.'
                NewArmor = self._resolve_mechanic(
                    mechanic=new_armor,
                    SuperClass=armor.Armor,
                    warning_message=msg,
                )
                new_armor = NewArmor()
            self.armor = new_armor

    def wield_shield(self, shield):
        """Accepts a string or Shield class and replaces the current armor.

        If a string is given, then a subclass of
        :py:class:`~dungeonsheets.armor.Shield` is retrived from the
        ``armor.py`` file. Otherwise, an subclass of
        :py:class:`~dungeonsheets.armor.Shield` can be provided
        directly.

        """
        if shield not in ("", "None", None):
            msg = 'Unknown shield "{}". Please ad it to ``shields.py``.'
            NewShield = self._resolve_mechanic(
                shield, SuperClass=armor.Shield, warning_message=msg
            )
            self.shield = NewShield()

    def wield_weapon(self, weapon):
        """Accepts a string and adds it to the list of wielded weapons.

        Parameters
        ----------
        weapon : str
          Case-insensitive string with a name of the weapon.

        """
        # Retrieve the weapon class from the weapons module
        msg = 'Unknown weapon "{}". Please add it to ``weapons.py``.'
        ThisWeapon = self._resolve_mechanic(
            mechanic=weapon,
            SuperClass=weapons.Weapon,
            warning_message=msg,
        )
        # Save it to the array
        self._weapons.append(ThisWeapon(wielder=self))

    @property
    def weapons(self):
        my_weapons = self._weapons.copy()
        # Account for unarmed strike
        if len(my_weapons) == 0 or hasattr(self, "Monk"):
            my_weapons.append(weapons.Unarmed(wielder=self))
        return my_weapons

    @property
    def hit_dice(self):
        """What type and how many dice to use for re-gaining hit points.

        To change, set hit_dice_num and hit_dice_faces."""
        dice_s = " + ".join([f"{c.level}d{c.hit_dice_faces}" for c in self.class_list])
        dice_s = combine_dice(dice_s)
        return dice_s

    @property
    def hit_dice_faces(self):
        # Not a valid function if multiclass
        if self.num_classes > 1:
            warnings.warn("hit_dice_faces is not valid for multiclass characters")
        return self.primary_class.hit_dice_faces

    @hit_dice_faces.setter
    def hit_dice_faces(self, faces):
        self.primary_class.hit_dice_faces = faces

    @property
    def proficiency_bonus(self):
        if self.level < 5:
            prof = 2
        elif 5 <= self.level < 9:
            prof = 3
        elif 9 <= self.level < 13:
            prof = 4
        elif 13 <= self.level < 17:
            prof = 5
        elif 17 <= self.level:
            prof = 6
        return prof

    def can_assume_shape(self, shape: monsters.Monster):
        return hasattr(self, "Druid") and self.Druid.can_assume_shape(shape)

    @property
    def all_wild_shapes(self):
        if hasattr(self, "Druid"):
            return self.Druid.all_wild_shapes
        else:
            return ()

    @property
    def wild_shapes(self):
        if hasattr(self, "Druid"):
            return self.Druid.wild_shapes
        else:
            return ()

    @wild_shapes.setter
    def wild_shapes(self, new_shapes):
        if hasattr(self, "Druid"):
            self.Druid.wild_shapes = new_shapes

    @property
    def ranger_beast(self):
        if hasattr(self, "Ranger"):
            return self.Ranger.ranger_beast
        else:
            return None

    @ranger_beast.setter
    def ranger_beast(self, beast):
        msg = f"Companion '{beast}' not found. Please add it to" " ``monsters.py``"
        beast = self._resolve_mechanic(beast, monsters.Monster, msg)
        self.Ranger.ranger_beast = (beast(), self.proficiency_bonus)

    @property
    def companions(self):
        """Return the list of companions and summonables"""
        companions = [compa for compa in self._companions]
        if self.ranger_beast:
            companions.append(self.ranger_beast)
        return companions

    @companions.setter
    def companions(self, compas):
        companions_list = []
        # Retrieve the actual monster classes if possible
        for compa in compas:
            msg = f"Companion '{compa}' not found. Please add it to" " ``monsters.py``"
            new_compa = self._resolve_mechanic(compa, monsters.Monster, msg)
            companions_list.append(new_compa())
        # Save the updated list for later
        self._companions = companions_list

    @property
    def infusions_text(self):
        if hasattr(self, "Artificer"):
            return tuple([i.name for i in self.infusions])
        else:
            return ()

    @classmethod
    def load(Cls, char_props: MutableMapping):
        """Factory Creates a character from the character definition.

        Parameters
        ==========
        char_props
          Keys and values holding all the attributes of the
          character. E.g. ``char_props['strength'] = 16``

        Returns
        =======
        char
          The initialized ``Character`` object with associated
          parameters.

        """
        # Parse the sheet type
        char_props.pop("sheet_type", "")
        # Load classes
        classes = char_props.get("classes", [])
        # backwards compatability
        if (len(classes) == 0) and ("character_class" in char_props):
            char_props["classes"] = [
                char_props.pop("character_class").lower().capitalize()
            ]
            char_props["levels"] = [str(char_props.pop("level"))]
        if 'Sorceror' in classes:
            classes.remove('Sorceror')
            classes.append('Sorcerer')
        # Create the character with loaded properties
        char = Cls(**char_props)
        log.info(f"Imported character: {char}")
        log.debug(f"New character classes: {char.class_list} ({char.levels})")
        log.debug(f"New character subclasses: {char.subclasses}")
        return char

    def save(self, filename, template_file="character_template.txt"):
        # Create the template context
        context = dict(
            char=self,
        )
        # Render the template
        src_path = os.path.join(os.path.dirname(__file__), "forms/")
        text = (
            jinja2.Environment(loader=jinja2.FileSystemLoader(src_path or "./"))
            .get_template(template_file)
            .render(context)
        )
        # Save the file
        with open(filename, mode="w") as f:
            f.write(text)

    def to_pdf(self, filename, **kwargs):
        from dungeonsheets.make_sheets import make_sheet

        if filename.endswith(".pdf"):
            filename = filename.replace("pdf", "py")
        make_sheet(filename, flatten=kwargs.get("flatten", True))


# Add backwards compatibility for tests
class Artificer(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Artificer"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Barbarian(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Barbarian"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Bard(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Bard"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Cleric(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Cleric"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Druid(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Druid"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Fighter(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Fighter"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Monk(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Monk"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Paladin(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Paladin"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Ranger(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Ranger"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Rogue(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Rogue"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Sorcerer(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Sorcerer"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Warlock(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Warlock"]
        attrs["levels"] = [level]
        super().__init__(**attrs)


class Wizard(Character):
    def __init__(self, level=1, **attrs):
        attrs["classes"] = ["Wizard"]
        attrs["levels"] = [level]
        super().__init__(**attrs)
