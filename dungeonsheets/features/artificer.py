from dungeonsheets import spells
from dungeonsheets.features.features import Feature, FeatureSelector


class _SpecialistSpells(Feature):
    """Starting at 3rd level, you always have certain spells pre­pared after
    you reach particular levels in this class, as shown in the Specializatin
    Spells table. These spells count as artificer spells for you, but they
    don't count against the number of artificer spells you prepare.
    """
    _name = "Select One"
    source = "Artificer"
    _spells = {
            3: [],
            5: [],
            9: [],
            13: [],
            17: []
            }
    spells_known = []
    spells_prepared = []

    @property
    def name(self):
        return "{:s} Spells".format(self._name)

    def __init__(self, owner=None):
        if owner is not None:
            level = owner.Artificer.level
            for lvl, spl in self._spells.items():
                if level >= lvl:
                    self.spells_known.extend(spl)
                    self.spells_prepared.extend(spl)
        super().__init__.(owner=owner)


class AlchemistSpells(_SpecialistSpells):
    """Starting at 3rd level, you always have certain spells pre­pared after
    you reach particular levels in this class, as shown in the Alchemist Spells
    table. These spells count as artificer spells for you, but they don't count
    against the number of artificer spells you prepare.
    """

    _name = "Alchemist"
    _spells = {
            3: [spells.HealingWord, spells.RayOfSickness],
            5: [spells.FlamingSphere, spells.MelfsAcidArrow],
            9: [spells.GaseousForm, spells.MassHealingWord],
            13: [spells.Blight, spells.DeathWard],
            17: [spells.Cloudkill, spells.RaiseDead]
            }


class ArtilleristSpells(_SpecialistSpells):
    """Starting at 3rd level, you always have certain spells prepared after
    you reach particular levels in this class, as shown  in the Artillerist
    Spells table. These spells count as artificer spells for you, but they
    don't count against the number of artificer spells you prepare.
    """

    _name = "Artillerist"
    _spells = {
            3: [spells.Shield, spells.Thunderwave],
            5: [spells.ScorchingRay, spells.Shatter],
            9: [spells.Fireball, spells.WindWall],
            13: [spells.IceStorm, spells.WallOfFire],
            17: [spells.ConeOfCold, spells.WallOfForce]
            }


class BattleSmithSpells(_SpecialistSpells):
    """Starting at 3rd level, you always have certain spells prepared after you
    reach particular levels in this class, as shown in the Battle Smith Spells
    table. These spells count as artificer spells for you, but they don't count
    against the number of artificer spells you prepare.
    """

    _name = "Battle Smith"
    _spells = {
            3: [spells.Heroism, spells.Shield],
            5: [spells.BrandingSmite, spells.WardingBond],
            9: [spells.AuraOfVitality, spells.ConjureBarrage],
            13: [spells.AuraOfPurity, spells.FireShield],
            17: [spells.BanishingSmite, spells.MassCureWounds]
            }


class FirearmProficiency(Feature):
    """The secrets of creating and operating gunpowder weapons have been
    discovered in various corners of the D&D multiverse. If your Dungeon Master
    uses the rules on firearms in chapter 9 of the Dungeon Master's Guide and
    your artificer has been exposed to the operation of such weapons, your
    artificer is proficient with them.
    """

    name = "Optional Rule: Firearm Proficiency"
    source = "Artificer"


class ToolProficiency(Feature):
    """At 3rd level, you choose the type of specialist you are: Alchemist,
    Artillerist, or Battle Smith, each of which is detailed at the end of the
    class's description. Your choice grants you features at 5th level and again
    at 9th and 15th level.
    """

    name = "Tool Proficiency"
    source = "Artificer (Alchemist)"


class AlchemicalSavant(Feature):
    """At 5th level, you develop masterful command of magical chemicals,
    enhancing the healing and damage you create through them. Whenever you
    cast a spell using your alchemist's supplies as the spellcasting focus, you
    gain a bonus to one roll of the spell. That roll must restore hit points or
    be a damage roll that deals acid, fire, necrotic, or poison damage, and the
    bonus equals your Intelli­gence modifier (minimum of +1).
    """

    name = "Alchemical Savant"
    source = "Artificer (Alchemist)"


class RestorativeReagents(Feature):
    """Starting at 9th level, you can incorporate
    restorative reagents into some of your works:
    - Whenever a creature drinks an experimental elixir you created, the
      creature gains temporary hit points equal to 2d6 + your Intelligence
      modifier (minimum of 1 temporary hit point).
    - You can cast lesser restoration without expending a spell slot and
      without preparing the spell, provided you use alchemist's supplies as the
      spellcasting focus. You can do so a number of times equal to your
      Intelligence modifier (minimum of once), and you regain all expended uses
      when you finish a long rest.
    """

    name = "Restorative Reagents"
    source = "Artificer (Alchemist)"


class ChemicalMastery(Feature):
    """By 15th level, you have been  exposed to so many chemicals that they
    pose little risk to you, and you can use them to quickly end certain
    ailments:
    - You gain resistance to acid damage and poison damage, and you are immune
      to the poisoned condition.
    - You can cast greater restoration and heal without expending a spell
      slot, without preparing the spell, and without material components,
      provided you use alchemist's supplies as the spellcasting focus. Once
      you cast either spell with this feature, you can't cast that spell with
      it again until you finish a long rest.
      """

      name = "Chemical Mastery"
      source = "Artificer (Alchemist)"


class MagicalTinkering(Feature):
    """At 1st level, you learn how to invest a spark of magic into mundane
    objects. To use this ability, you must have tinker's tools or other
    artisan's tools  in hand. You then touch a Tiny nonmagical object as an
    action and give it one of the following magical properties of your choice:
    - The object sheds bright light in a 5-foot radius and dim light for an
      additional 5 fe et.
    - Whenever tapped by a creature, the object emits a recorded message that
      can be heard up to 10 feet away. You utter the message when you bestow
      this property on the object, and the recording can be no more than 6
      seconds long.
    - The object continuously emits your choice of an odor or a nonverbal sound
      (wind, waves, chirping, or the like). The chosen phenomenon is
      perceivable up to  10 feet away.
    - A static visual effect appears on one of the object's surfaces. This
      effect can be a picture, up to 25 words of text, lines and shapes, or a
      mixture of these elements, as you like. The chosen property lasts
      indefinitely. As an action, you can touch the object and end the property
      early. You can bestow magic on multiple objects, touching one object each
      time you use this feature, though a single  object can only bear one
      property at a time. The maximum number of objects you can affect with
      this feature at one time is equal to your Intelligence modifier (minimum
      of one object). If you try to exceed your maximum, the oldest property
      immediately ends, and then the new property applies.
      """

      name = "Magical Tinkering"
      source = "Artificer"


class InfuseItem(Feature):
    """At 2nd level, you gain the ability to imbue mundane items with certain
    magical infusions. The magic items you create with this feature are
    effectively prototypes of permanent items.

    INFUSIONS KNOWN
    When you gain this feature, pick four artificer infusions
    to learn, choosing from the "Artificer Infusions" section at the end of the
    class's description. You learn additional infusions of your choice when you
    reach certain levels in this class, as shown in the Infusions Known column
    of the Artificer table. Whenever you gain a level in this class, you can
    re­place one of the artificer infusions you learned with a new one.

    INFUSING AN ITEM
    Whenever you finish a long rest, you can touch a non­magical object and
    imbue it with one of your artificer in­fusions, turning it into a magic
    item. An infusion works on only certain kinds of objects, as specified in
    the infusion's description. If the item requires attunement, you can
    attune yourself to it the instant you infuse the item. If you decide to
    attune to the item later, you must do so using the normal process for
    attunement (see "Attunement" in chapter 7 of the Dungeon Master's Guide).
    Your infusion remains in an item indefinitely, but when you die, the
    infusion vanishes after a number of days have passed equal to your
    Intelligence modifier (minimum of 1 day). The infusion also vanishes if you
    give up your knowledge of the infusion for another one. You can infuse more
    than one nonmagical object at the end of a long rest; the maximum number of
    objects appears in the Infused Items column of the Artificer table. You
    must touch each of the objects, and each of your infusions can be in only
    one object at a time. Moreover, no object can bear more than one of your
    infusions at a time. If you try to exceed your maximum number of
    in­fusions,  the  oldest infusion immediately ends, and then the new
    infusion applies.
    """

    _name = "Infuse Item"
    source = "Artificer"
    _infusions = {
            # level: (infusions known, infused items)
            2:  (4, 2),
            3:  (4, 2),
            4:  (4, 2),
            5:  (4, 2),
            5:  (4, 2),
            6:  (6, 3),
            7:  (6, 3),
            8:  (6, 3),
            9:  (6, 3),
            10: (8, 4),
            11: (8, 4),
            12: (8, 4),
            13: (8, 4),
            14: (10, 5),
            15: (10, 5),
            16: (10, 5),
            17: (10, 5),
            18: (12, 6),
            19: (12, 6),
            20: (12, 6),
            }


    @property
    def name(self):
        known_infusions = self._infusions[self.owner.Artificer.level][0]
        infused_items = self._infusions[self.owner.Artificer.level][1]
        return self._name + " ({:d} Infusions Known, {:d} Infused Items".format(
                known_infusions, infused_items)



class TheRightToolForTheJob(Feature):
    """At 3rd level, you learn how to produce exactly the tool you need: with
    tinker's tools in hand, you can magically create one set of artisan's tools
    in an unoccupied space within 5 feet of you. This creation requires  1
    hour of uninterrupted work, which can coincide with a short or long rest.
    Though the product of magic, the tools are nonmagical, and they vanish when
    you use this fea­ture again.
    """

    name = "The Right Tool For The Job"
    source = "Artificer"


class ToolExpertise(Feature):
    """Starting at 6th level, your proficiency bonus is doubled for any ability
    check you make that uses your proficiency with a tool.
    """

    name = "Tool Expertise"
    source = "Artificer"


class FlashOfGenius(Feature):
    """Starting at 7th level, you gain the ability to come up with solutions
    under pressure. When you or another creature you can see within 30 feet of
    you makes an ability check or a saving throw, you can use your reaction to
    add your Intelligence modifier to the roll. You can use this feature a
    number of times equal to your Intelligence modifier (minimum of once). You
    re­gain all expended uses when you finish a long rest.
    """

    name = "Flash Of Genius"
    source = "Arificer"


class MagicItemAdept(Feature):
    """When you reach 10th level, you achieve a profound un­derstanding of how
    to use and make magic items:
    - You can attune to up to four magic items at once.
    - If you craft a magic item with a rarity of common or uncommon, it takes
      you a quarter of the normal time, and it costs you half as much of the
      usual gold.
      """

      name = "Magic Item Adept"
      source = "Artificer"


class SpellStoringItem(Feature):
    """At 11th level, you learn how to store a spell in an object. Whenever you
    finish a long rest, you can touch one simple or martial weapon or one item
    that you can use as a spellcasting focus, and you store a spell in it,
    choosing a  1st- or 2nd-level spell from the artificer spell list that
    requires 1 action to cast (you needn't have it prepared).

    While holding the object, a creature can take an action to produce the
    spell's effect from it, using your spellcast­ing ability modifier. If the
    spell requires concentration, the creature must concentrate. The spell
    stays in the ob­ject until it's been used a number of times equal to twice
    your Intelligence  modifier (minimum of twice) or until you use this fe
    ature again to store a spell in an object.
    """

    name = "Spell-Storing Item"
    source = "Artificer"


class MagicItemSavant(Feature):
    """At 14th level, your skill with magic items deepens more:
    - You can attune to up to five magic items at once.
    - You ignore all class, race, spell, and level require­ments on attuning to
      or using a magic item.
    """

    name = "Magic Item Savant"
    source = "Artificer"


class MagicItemMaster(Feature):
    """Starting at  18th level, you can attune to up to six magic items at
    once.
    """

    name = "Magic Item Master"
    source = "Artificer"


class SoulOfArtifice(Feature):
    """At 20th level, you develop a mystical connection to your magic items,
    which you can draw on for protection:
    - You gain a +1 bonus to all saving throws per magic item you are currently
      attuned to.
    - If you're reduced to 0 hit points but not killed out­right, you can use
      your reaction to end one of your artificer infusions, causing you to drop
      to  1  hit point instead of 0.
    """

    name = "Soul Of Artifice"
    source = "Artificer"
