from dungeonsheets import weapons
from dungeonsheets.features.features import Feature, FeatureSelector
from dungeonsheets.features.rogue import Evasion, UncannyDodge


# PHB
class FavoredEnemy(Feature):
    """Beginning at 1st level, you have significant experience studying, tracking,
    hunting, and even talking to a certain type of enemy.

    Choose a type of favored enemy: aberrations, beasts, celestials,
    constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes,
    plants, or undead. Alternatively, you can select two races of humanoid
    (such as gnolls and orcs) as favored enemies. You have advantage on Wisdom
    (Survival) checks to track your favored enemies, as well as on Intelligence
    checks to recall information about them.

    When you gain this feature, you also learn one language of your choice that
    is spoken by your favored enemies, if they speak one at all. You choose one
    additional favored enemy, as well as an associated language, at 6th and
    14th level. As you gain levels, your choices should reflect the types of
    monsters you have encountered on your adventures.

    """

    name = "Favored Enemy"
    source = "Ranger"
    languages = ("[Select One]",)


class NaturalExplorer(Feature):
    """You are particularly familiar with one type of natural environment
    and are adept at traveling and surviving in such regions. Choose
    one type of favored terrain: arctic, coast, desert, forest,
    grassland, mountain, swamp, or the Underdark. You choose
    additional favored terrain types at 6th and 10th

    When you make an Intelligence or Wisdom check related to your
    favored terrain, your proficiency bonus is doubled if you are
    using a skill that you're proficient in. While traveling for an
    hour or more in your favored terrain, you gain the following
    benefits:

    - Difficult terrain doesn't slow your group's travel.
    - Your group can't become lost except by magical means.
    - Even when you are engaged in another activity while traveling
      (such as foraging, navigating, or tracking), you remain alert to
      danger.
    - If you are traveling alone, you can move stealthily at a normal
      pace.
    - When you forage, you find twice as much food as you normally
      would.
    - While tracking other creatures, you also learn their exact
      number, their sizes, and how long ago they passed through the
      area.

    """

    name = "Natural Explorer"
    source = "Ranger"


class Archery(Feature):
    """
    You gain a +2 bonus to attack rolls you make
    with ranged weapons (included in stats on Character Sheet).
    """

    name = "Fighting Style (Archery)"
    source = "Ranger"

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        +2 attack roll bonus if weapon is ranged
        """
        if isinstance(weapon, weapons.RangedWeapon):
            weapon.attack_bonus += 2


class Defense(Feature):
    """
    While you are wearing armor, you gain a +1 bonus to AC (included in
    stats on Character Sheet).
    """

    name = "Fighting Style (Defense)"
    source = "Ranger"


class Dueling(Feature):
    """When you are wielding a melee weapon in one hand and no other weapons, you
    gain a +2 bonus to damage rolls with that weapon.

    """

    name = "Fighting Style (Dueling)"
    source = "Ranger"

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        +2 attack roll bonus if melee weapon is not two handed
        """
        if (
            isinstance(weapon, weapons.MeleeWeapon)
            and "two-handed" not in weapon.properties.lower()
        ):
            weapon.damage_bonus += 2


class TwoWeaponFighting(Feature):
    """When you engage in two-weapon fighting, you can add your ability modifier
    to the damage of the second attack.

    """

    name = "Fighting Style (Two-Weapon Fighting)"
    source = "Ranger"


class GreatWeaponFighting(Feature):
    """When you roll a 1 or 2 on a damage die for an attack you make with a melee
    weapon that you are wielding with two hands, you can reroll the die and
    must use the new roll, even if the new roll is a 1 or a 2. The weapon must
    have the two-handed or versatile property for you to gain this benefit.
    """

    name = "Fighting Style (Great Weapon Fighting)"
    source = "Blood Hunter"


class RangerFightingStyle(FeatureSelector):
    """
    Select a Fighting Style by choosing in feature_choices:

    archery

    defense

    dueling

    two-weapon fighting
    """

    options = {
        "archery": Archery,
        "defense": Defense,
        "dueling": Dueling,
        "two-weapon fighting": TwoWeaponFighting,
        "two-weapon": TwoWeaponFighting,
        "dual wield": TwoWeaponFighting,
    }
    name = "Fighting Style (Select One)"
    source = "Ranger"


class PrimevalAwareness(Feature):
    """Beginning at 3rd level, you can use your action and expend one ranger spell
    slot to focus your awareness on the region around you. For 1 minute per
    level of the spell slot you expend, you can sense whether the following
    types of creatures are present within 1 mile of you (or within up to 6
    miles if you are in your favored terrain): aberrations, celestials,
    dragons, elementals, fey, fiends, and undead. This feature doesn't reveal
    the creatures' location or number.

    """

    name = "Primeval Awareness"
    source = "Ranger"


class ExtraAttackRanger(Feature):
    """Beginning at 5th level, you can attack twice, instead of once, whenever you
    take the Attack action on your turn.

    """

    name = "Extra Attack (2x)"
    source = "Ranger"


class HideInPlainSight(Feature):
    """Starting at 10th level, you can spend 1 minute creating camouflage for
    yourself. You must have access to fresh mud, dirt, plants, soot, and other
    naturally occurring materials with which to create your camouflage. Once
    you are camouflaged in this way, you can try to hide by pressing yourself
    up against a solid surface, such as a tree or wall, that is at least as
    tall and wide as you are.

    You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain
    there without moving or taking actions. Once you move or take an action or
    a reaction, you must camouflage yourself again to gain this benefit

    """

    name = "Hide in Plain Sight"
    source = "Ranger"


class Vanish(Feature):
    """Starting at 14th level, you can use the Hide action as a bonus action on
    your turn. Also, you can't be tracked by nonmagical means, unless you
    choose to leave a trail.

    """

    name = "Vanish"
    source = "Ranger"


class FeralSenses(Feature):
    """At 18th level, you gain preternatural senses that help you fight creatures
    you can't see. When you attack a creature you can't see, your inability to
    see it doesn't impose disadvantage on your attack rolls against it. You are
    also aware of the location of any invisible creature within 30 feet of you,
    provided that the creature isn't hidden from you and you aren't blinded or
    deafened

    """

    name = "Feral Senses"
    source = "Ranger"


class FoeSlayer(Feature):
    """At 20th level, you become an unparalleled hunter of your enemies. Once on
    each of your turns, you can add your Wisdom modifier to the attack roll or
    the damage roll of an attack you make against one o f your favored
    enemies. You can choose to use this feature before or after the roll, but
    before any effects of the roll are applied.

    """

    name = "Foe Slayer"
    source = "Ranger"


# Hunter
class ColossusSlayer(Feature):
    """Your tenacity can wear down the most potent foes. When you hit a creature
    with a weapon attack, the creature takes an extra 1d8 damage if it's below
    its hit point maximum. You can deal this extra damage only once per turn.

    """

    name = "Colossus Slayer"
    source = "Ranger (Hunter)"


class GiantKiller(Feature):
    """When a Large or larger creature within 5 feet of you hits or misses you
    with an attack, you can use your reaction to attack that creature
    immediately after its attack, provided that you can see the creature.

    """

    name = "Giant Killer"
    source = "Ranger (Hunter)"


class HordeBreaker(Feature):
    """Once on each o f your turns when you make a weapon attack, you can make
    another attack with the same weapon against a different creature that is
    within 5 feet of the original target and within range of your weapon.

    """

    name = "Horde Breaker"
    source = "Ranger (Hunter)"


class HuntersPrey(FeatureSelector):
    """Select a Hunter's Prey option in "feature_choices" in your .py file from
    one of:

    colossus slayer

    giant killer

    horde breaker

    """

    options = {
        "colossus slayer": ColossusSlayer,
        "giant killer": GiantKiller,
        "horde breaker": HordeBreaker,
    }
    name = "Hunter's Prey (Select One)"
    source = "Ranger (Hunter)"


class EscapeTheHorde(Feature):
    """Opportunity attacks against you are made with disadvantage"""

    name = "Escape the Horde"
    source = "Ranger (Hunter)"


class MultiattackDefense(Feature):
    """When a creature hits you with an attack, you gain a +4 bonus to AC against
    all subsequent attacks made by that creature for the rest of the turn.

    """

    name = "Multiattack Defense"
    source = "Ranger (Hunter)"


class SteelWill(Feature):
    """You have advantage on saving throws against being frightened."""

    name = "Steel Will"
    source = "Ranger (Hunter)"


class DefensiveTactics(FeatureSelector):
    """Select a Defensive Tactics option in "feature_choices" in your .py file from
    one of:

    escape the horde

    multiattack defense

    steel will

    """

    options = {
        "escape the horde": EscapeTheHorde,
        "multiattack defense": MultiattackDefense,
        "steel will": SteelWill,
    }
    name = "Defensive Tactics (Select One)"
    source = "Ranger (Hunter)"


class Volley(Feature):
    """You can use your action to make a ranged attack against any number of
    creatures within 10 feet o f a point you can see within your weapon's
    range. You must have ammunition for each target, as normal, and you make a
    separate attack roll for each target

    """

    name = "Volley"
    source = "Ranger (Hunter)"


class WhirlwindAttack(Feature):
    """You can use your action to make a melee attack against any number o f
    creatures within 5 feet of you, with a separate attack roll for each target

    """

    name = "Whirlwind Attack"
    source = "Ranger (Hunter)"


class MultiattackRanger(FeatureSelector):
    """Select a Multiattack option in "feature_choices" in your .py file from
    one of:

    volley

    whirlwind attack

    """

    options = {"volley": Volley, "whirlwind attack": WhirlwindAttack}
    name = "Multiattack (Select One)"
    source = "Ranger (Hunter)"


class StandAgainstTheTide(Feature):
    """When a hostile creature misses you with a melee attack, you can use your
    reaction to force that creature to repeat the same attack against another
    creature (other than itself) of your choice

    """

    name = "Stand Against the Tide"
    source = "Ranger (Hunter)"


class SuperiorHuntersDefense(FeatureSelector):
    """Select a Superior Hunter's Defense option in "feature_choices" in your .py
    file from one of:

    evasion

    stand against the tide

    uncanny dodge

    """

    options = {
        "evasion": Evasion,
        "stand against of the tide": StandAgainstTheTide,
        "uncanny dodge": UncannyDodge,
    }
    name = "Superior Hunter's Defense (Select One)"
    source = "Ranger (Hunter)"


# Beast Master
class RangersCompanion(Feature):
    """At 3rd level, you gain a beast companion that accompanies you on your
    adventures and is trained to fight alongside you. Choose a beast that is no
    larger than Medium and that has a challenge rating of 1/4 or lower
    (appendix D presents statistics for the hawk, mastiff, and panther as
    examples). Add your proficiency bonus to the beast's AC, attack rolls, and
    damage rolls, as well as to any saving throws and skills it is proficient
    in. Its hit point maximum equals its normal maximum or four times your
    ranger level, whichever is higher.

    The beast obeys your commands as best as it can. It takes its turn on your
    initiative, though it doesn't take an action unless you command it to. On
    your turn, you can verbally command the beast where to move (no action
    required by you). You can use your action to verbally command it to take
    the Attack, Dash, Disengage, Dodge, or Help action. Once you have the Extra
    Attack feature, you can make one weapon attack yourself when you command
    the beast to take the Attack action.

    While traveling through your favored terrain with only the beast, you can
    move stealthily at a normal pace. If the beast dies, you can obtain another
    one by spending 8 hours magically bonding with another beast that isn't
    hostile to you, either the same type of beast as before or a different one.

    """

    name = "Ranger's Companion"
    source = "Ranger (Beast Master)"


class ExceptionalTraining(Feature):
    """Beginning at 7th level, on any of your turns when your beast companion
    doesn't attack, you can use a bonus action to command the beast to take the
    Dash, Disengage, Dodge, or Help action on its turn

    """

    name = "Exceptional Training"
    source = "Ranger (Beast Master)"


class BestialFury(Feature):
    """Starting at 11th level, your beast companion can make two attacks when you
    command it to use the Attack action.

    """

    name = "Bestial Fury"
    source = "Ranger (Beast Master)"


class ShareSpells(Feature):
    """Beginning at 15th level, when you cast a spell targeting yourself, you can
    also affect your beast companion with the spell if the beast is within 30
    feet of you

    """

    name = "Share Spells"
    source = "Ranger (Beast Master)"


# Gloom Stalker
class DreadAmbusher(Feature):
    """At 3rd level, you master the art of the ambush. You can give yourself a
    bonus to your initiative rolls equal to your Wisdom modifier. At the start
    of your first turn of each combat, your walking speed increases by 10 feet,
    which lasts until the end of that turn. If you take the Attack action on
    that turn, you can make one additional weapon attack as part of that
    action. If that attack hits, the target takes an extra 1d8 damage of the
    weapons damage type.

    """

    name = "Dread Ambusher"
    source = "Ranger (Gloom Stalker)"


class UmbralSight(Feature):
    """At 3rd level, you gain darkvision out to a range of 60 feet. If you already
    have darkvision from your race, its range increases by 30 feet. You are
    also adept at evading creatures that rely on darkvision. While in darkness,
    you are invisible to any creature that relies on darkvision to see you in
    that darkness.

    """

    name = "Umbral Sight"
    source = "Ranger (Gloom Stalker)"


class IronMind(Feature):
    """By 7th level, you have honed your ability to resist the mind-altering
    powers of your prey. You gain proficiency in Wisdom saving throws. Ifyou
    already have this proficiency, you instead gain proficiency in
    Intelligence or Charisma saving throws (your choice)

    """

    name = "Iron Mind"
    source = "Ranger (Gloom Stalker)"
    needs_implementation = True

    def __init__(self, owner=None):
        super().__init__(owner=owner)


class StalkersFlurry(Feature):
    """At 11th level, you learn to attack with such unexpected speed that you can
    turn a miss into another strike. Once on each of your turns when you miss
    with a weapon attack, you can make another weapon attack as part of the
    same action

    """

    name = "Stalker's Flurry"
    source = "Ranger (Gloom Stalker)"


class ShadowyDodge(Feature):
    """Starting at 15th level, you can dodge in unforeseen ways, with wisps of
    supernatural shadow around you. Whenever a creature makes an attack roll
    against you and doesn't have advantage on the roll, you can use your
    reaction to impose disadvantage on it. You must use this feature before you
    know the outcome of the attack roll.

    """

    name = "Shadowy Dodge"
    source = "Ranger (Gloom Stalker)"


# Horizon Walker
class DetectPortal(Feature):
    """At 3rd level, you gain the ability to magically sense the presence of a
    planar portal. As an action, you detect the distance and direction to the
    closest planar portal within 1 mile of you. Once you use this feature, you
    can't use it again until you finish a short or long rest.

    """

    name = "Detect Portal"
    source = "Ranger (Horizon Walker)"


class PlanarWarrior(Feature):
    """At 3rd level, you learn to draw on the energy of the multiverse to
    augment your attacks. As a bonus action, choose one creature you can see
    within 30 feet of you. The next time you hit that creature on this turn
    with a weapon attack, all damage dealt by the attack becomes force damage,
    and the creature takes an extra 1d8 force damage from the attack. When you
    reach 11th level in this class, the extra damage increases to 2d8.

    """

    _name = "Planar Warrior"
    source = "Ranger (Horizon Walker)"

    @property
    def name(self):
        if self.owner.Ranger.level < 11:
            return self._name + " (1d8/f)"
        else:
            return self._name + " (2d8/f)"


class EtherealStep(Feature):
    """At 7th level, you learn to step through the Ethereal Plane. As a bonus
    action, you can cast the etherealncss spell with this feature, without
    expending a spell slot, but the spell ends at the end of the current
    turn. Once you use this feature, you can't use it again until you finish a
    short or long rest

    """

    name = "Ethereal Step"
    source = "Ranger (Horizon Walker)"


class DistantStrike(Feature):
    """At 11th level, you gain the ability to pass between the planes in the blink
    of an eye. When you take the Attack action, you can teleport up to 10 feet
    before each attack to an unoccupied space you can see. Ifyou attack at
    least two different creatures with the action, you can make one additional
    attack with it against a third creature.

    """

    name = "Distant Strike"
    source = "Ranger (Horizon Walker)"


class SpectralDefense(Feature):
    """At 15th level, your ability to move between planes enables you to slip
    through the planar boundaries to lessen the harm done to you during
    battle. When you take damage from an attack, you can use your reaction to
    give yourself resistance to all of that attack's damage on this turn

    """

    name = "Spectral Defense"
    source = "Ranger (Horizon Walker)"


# Monster Slayer
class HuntersSense(Feature):
    """At 3rd level, you gain the ability to peer at a creature and magically
    discern how best to hurt it. As an action, choose one creature you can see
    within 60 feet ofyou. You immediately learn whether the creature has any
    damage immunities, resistances, or vulnerabilities and What they are. If
    the creature is hidden from divination magic, you sense that it has no
    damage immunities, re- sistances, or vulnerabilities. You can use this
    feature a number of times equal to your Wisdom modifier (minimum of
    once). You regain all expended uses of it when you finish a long rest.

    """

    _name = "Hunter's Sense"
    source = "Ranger (Monster Slayer)"

    @property
    def name(self):
        num = max(1, self.owner.wisdom.modifier)
        return self._num + " ({:d}x/LR)".format(num)


class SlayersPrey(Feature):
    """Starting at 3rd level, you can focus your ire on one foe, increasing the
    harm you inflict on it. As a bonus action, you designate one creature you
    can see within 60 feet of you as the target of this feature. The first time
    each turn that you hit that target with a weapon attack, it takes an extra
    1d6 damage from the weapon. This benefit lasts until you finish a short or
    long rest. It ends early if you designate a different creature

    """

    name = "Slayer's Prey"
    source = "Ranger (Monster Slayer)"


class SupernaturalDefense(Feature):
    """At 7th level, you gain extra resilience against your prey's assaults on
    your mind and body. Whenever the target of your Slayer's Prey forces you to
    make a saving throw and whenever you make an ability check to escape that
    targets grapple, add 1d6 to your roll

    """

    name = "Supernatural Defense"
    source = "Ranger (Monster Slayer)"


class MagicUsersNemesis(Feature):
    """At 11th level, you gain the ability to thwart someone else's magic. When
    you see a creature casting a spell or teleporting within 60 feet of you,
    you can use your reaction to try to magically foil it. The creature must
    succeed on a Wisdom saving throw against your spell save DC, or its spell
    or teleport fails and is wasted. Once you use this feature, you can't use
    it again until you finish a short or long rest.

    """

    name = "Magic User's Nemesis"
    source = "Ranger (Monster Slayer)"


class SlayersCounter(Feature):
    """At 15th level, you gain the ability to counterattack when your prey tries
    to sabotage you. If the target of your Slayer's Prey forces you to make a
    saving throw, you can use your reaction to make one weapon attack against
    the quarry. You make this attack immediately before making the saving
    throw. If your attack hits, your save automatir cally succeeds, in addition
    to the attack's normal effects

    """

    name = "Slayer's Counter"
    source = "Ranger (Monster Slayer)"


# Revised Ranger
class FavoredEnemyRevised(Feature):
    """Beginning at 1st level, you have significant experience studying, tracking,
    hunting, and even talking to a certain type of enemy commonly encountered
    in the wilds.

    Choose a type of favored enemy: beasts, fey, humanoids, monstrosities, or
    undead. You gain a +2 bonus to damage rolls with weapon attacks against
    creatures of the chosen type. Additionally, you have advantage on Wisdom
    (Survival) checks to track your favored enemies, as well as on Intelligence
    checks to recall information about them.

    When you gain this feature, you also learn one language of your choice,
    typically one spoken by your favored enemy or creatures associated with
    it. However, you are free to pick any language you wish to learn

    """

    name = "Favored Enemy"
    source = "Revised Ranger"


class NaturalExplorerRevised(Feature):
    """You are a master of navigating the natural world, and you react
    with swift and decisive action when attacked. This grants you the
    following benefits:

    - You ignore difficult terrain.
    - You have advantage on initiative rolls.
    - On your first turn during combat, you have advantage on attack rolls
      against creatures that have not yet acted.

    In addition, you are skilled at navigating the wilderness. You
    gain the following benefits when traveling for an hour or more:

    - Difficult terrain doesn't slow your group's travel.
    - Your group can't become lost except by magical means.
    - Even when you are engaged in another activity while traveling
      (such as foraging, navigating, or tracking), you remain alert to
      danger.
    - If you are traveling alone, you can move stealthily at a normal
      pace.
    - When you forage, you find twice as much food as you normally
      would.
    - While tracking other creatures, you also learn their exact
      number, their sizes, and how long ago they passed through the
      area.

    """

    name = "Natural Explorer"
    source = "Revised Ranger"


class PrimevalAwarenessRevised(Feature):
    """Beginning at 3rd level, your mastery of ranger lore allows you to establish
    a powerful link to beasts and to the land around you.

    You have an innate ability to communicate with beasts, and they recognize
    you as a kindred spirit. Through sounds and gestures, you can communicate
    simple ideas to a beast as an action, and can read its basic mood and
    intent. You learn its emotional state, whether it is affected by magic of
    any sort, its short-term needs (such as food or safety), and actions you
    can take (if any) to persuade it to not attack.

    You cannot use this ability against a creature that you have attacked
    within the past 10 minutes.

    Additionally, you can attune your senses to determine if any of your
    favored enemies lurk nearby. By spending 1 uninterrupted minute in
    concentration (as if you were concentrating on a spell), you can sense
    whether any of your favored enemies are present within 5 miles of you. This
    feature reveals which of your favored enemies are present, their numbers,
    and the creatures' general direction and distance (in miles) from you.

    If there are multiple groups of your favored enemies within range, you
    learn this information for each group.

    """

    name = "Primeval Awareness"
    source = "Revised Ranger"


class GreaterFavoredEnemy(Feature):
    """At 6th level, you are ready to hunt even deadlier game. Choose a type of
    greater favored enemy: aberrations, celestials, constructs, dragons,
    elementals, fiends, or giants. You gain all the benefits against this
    chosen enemy that you normally gain against your favored enemy, including
    an additional language. Your bonus to damage rolls against all your favored
    enemies increases to +4.

    Additionally, you have advantage on saving throws against the spells and
    abilities used by a greater favored enemy.

    """

    name = "Greated Favored Enemy"
    source = "Revised Ranger"


class FleetOfFoot(Feature):
    """Beginning at 8th level, you can use the Dash action as a bonus action on
    your turn.

    """

    name = "Fleet of Foot"
    source = "Revised Ranger"


class HideInPlainSightRevised(Feature):
    """Starting at 10th level, you can remain perfectly still for long periods of
    time to set up ambushes.

    When you attempt to hide on your turn, you can opt to not move on that
    turn. If you avoid moving, creatures that attempt to detect you take a −10
    penalty to their Wisdom (Perception) checks until the start of your next
    turn. You lose this benefit if you move or fall prone, either 4 voluntarily
    or because of some external effect. You are still automatically detected if
    any effect or action causes you to no longer be hidden.

    If you are still hidden on your next turn, you can continue to remain
    motionless and gain this benefit until you are detected

    """

    name = "Hide in Plain Sight"
    source = "Revised Ranger"


# Beast Conclave
class AnimalCompanion(Feature):
    """At 3rd level, you learn to use your magic to create a powerful bond with a
    creature of the natural world.

    With 8 hours of work and the expenditure of 50 gp worth of rare herbs and
    fine food, you call forth an animal from the wilderness to serve as your
    faithful companion. You normally select you companion from among the
    following animals: an ape, a black bear, a boar, a giant badger, a giant
    weasel, a mule, a panther, or a wolf. However, your DM might pick one of
    these animals for you, based on the surrounding terrain and on what types
    of creatures would logically be present in the area.

    At the end of the 8 hours, your animal companion appears and gains all the
    benefits of your Companion's Bond ability. You can have only one animal
    companion at a time.

    If your animal companion is ever slain, the magical bond you share allows
    you to return it to life. With 8 hours of work and the expenditure of 25 gp
    worth of rare herbs and fine food, you call forth your companion's spirit
    and use your magic to create a new body for it. You can return an animal
    companion to life in this manner even if you do not possess any part of its
    body.

    If you use this ability to return a former animal companion to life while
    you have a current animal companion, your current companion leaves you and
    is replaced by the restored companion

    """

    name = "Animal Companion"
    source = "Revised Ranger (Animal Companion)"


class CompanionsBond(Feature):
    """Your animal companion gains a variety of benefits while it is linked to
    you. The animal companion loses its Multiattack action, if it has one.

    The companion obeys your commands as best it can. It rolls for initiative
    like any other creature, but you determine its actions, decisions,
    attitudes, and so on. If you are incapacitated or absent, your companion
    acts on its own. When using your Natural Explorer feature, you and your
    animal companion can both move stealthily at a normal pace.

    Your animal companion has abilities and game statistics determined in part
    by your level. Your companion uses your proficiency bonus rather than its
    own. In addition to the areas where it normally uses its proficiency bonus,
    an animal companion also adds its proficiency bonus to its AC and to its
    damage rolls.

    Your animal companion gains proficiency in two skills of your choice. It
    also becomes proficient with all saving throws. For each level you gain
    after 3rd, your animal companion gains an additional hit die and increases
    its hit points accordingly. Whenever you gain the Ability Score Improvement
    class feature, your companion's abilities also improve. Your companion can
    increase one ability score of your choice by 2, or it can increase two
    ability scores of your choice by 1. As normal, your companion can't
    increase an ability score above 20 using this feature unless its
    description specifies otherwise.

    Your companion shares your alignment, and has a personality trait and a
    flaw that you can roll for or select from the tables below. Your companion
    shares your ideal, and its bond is always, \"The ranger who travels with me
    is a beloved companion for whom I would gladly give my life.\"

    """

    name = "Companions Bond"
    source = "Revised Ranger (Beast Conclave)"


class CoordinatedAttack(Feature):
    """Beginning at 5th level, you and your animal companion form a more potent
    fighting team. When you use the Attack action on your turn, if your
    companion can see you, it can use its reaction to make a melee attack.
    """

    name = "Coordinated Attack"
    source = "Revised Ranger (Beast Conclave)"


class BeastsDefense(Feature):
    """At 7th level, while your companion can see you, it has advantage on all
    saving throw

    """

    name = "Beast's Defense"
    source = "Revised Ranger (Beast Conclave)"


class StormOfClawsAndFangs(Feature):
    """At 11th level, your companion can use its action to make a melee attack
    against each creature of its choice within 5 feet of it, with a separate
    attack roll for each target

    """

    name = "Storm of Claws and Fangs"
    source = "Revised Ranger (Beast Conclave)"


class SuperiorBeastsDefense(Feature):
    """At 15th level, whenever an attacker that your companion can see hits it
    with an attack, it can use its reaction to halve the attack's damage
    against it.

    """

    name = "Superior Beast's Defense"
    source = "Revised Ranger (Beast Conclave)"


# Deep Stalker Conclave
class UnderdarkScout(Feature):
    """At 3rd level, you master the art of the ambush. On your first turn during
    combat, you gain a +10 bonus to your speed, and if you use the Attack
    action, you can make one additional attack. You are also adept at evading
    creatures that rely on darkvision. Such creatures gain no benefit when
    attempting to detect you in dark and dim conditions. Additionally, when the
    DM determines if you can hide from a creature, that creature gains no
    benefit from its darkvision

    """

    name = "Underdark Scout"
    source = "Revised Ranger (Deep Stalker Conclave)"


class StalkersDodge(Feature):
    """At 15th level, whenever a creature attacks you and does not have advantage,
    you can use your reaction to impose disadvantage on the creature's attack
    roll against you. You can use this feature before or after the attack roll
    is made, but it must be used before the outcome of the roll is determined

    """

    name = "Stalker's Dodge"
    source = "Revised Ranger (Deep Stalker Conclave)"
    

#Blood Hunter
class HunterBane(Feature):
    """Beginning at 1st level, you have survived the Hunter’s Bane, a dangerous, long-guarded ritual that alters your life’s blood, forever binding you to the darkness and honing your senses against it. You have advantage on Wisdom (Survival) checks to track fey, fiends, or undead, as well as on Intelligence ability checks to recall information about them.

The Hunter’s Bane also empowers your body to control and shape hemocraft magic, using your own blood and life essence to fuel your abilities. Some of your features require your target to make a saving throw to resist the feature’s effects. The saving throw DC is calculated as follows:

Hemocraft save DC = 8 + your proficiency bonus + your Intelligence modifier.

    """

    name = "Hunter's Bane"
    source = "Blood Hunter"


class BloodMaledict(Feature):
    """At 1st level, you gain the ability to channel, and sometimes sacrifice, a part of your vital essence to curse and manipulate creatures through hemocraft magic. You gain one blood curse of your choice, detailed in the “Blood Curses” section at the end of the class description. You learn one additional blood curse of your choice, and you can choose one of the blood curses you know and replace it with another blood curse, at 6th, 10th, 14th, and 18th level.

When you use your Blood Maledict, you choose which curse to invoke. While invoking a blood curse, but before it affects the target, you can choose to amplify the curse by losing a number of hit points equal to one roll of your hemocraft die, as shown in the Hemocraft Die column of the Blood Hunter table. An amplified curse gains an additional effect, noted in the curse’s description. Creatures that do not have blood in their bodies are immune to blood curses, unless you have amplified the curse.

You can use this feature once. Beginning at 6th level, you can use your Blood Maledict feature twice, at 13th level you can use it three times between rests, and at 17th level, you can use it four times between rests. You regain all expended uses when you finish a short or long rest.

    """

    name = "Blood Maledict"
    source = "Blood Hunter"


class BloodHunterFightingStyle(FeatureSelector):
    """At 2nd level, you adopt a style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again.
Archery

You gain a +2 bonus to attack rolls you make with ranged weapons.

Dueling

When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.

Great Weapon Fighting

When you roll a 1 or 2 on a non-rite damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll. The weapon must have the two-handed or versatile property for you to gain this benefit.

Two-Weapon Fighting

When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.

    """
    
    options = {
    	"archery": Archery,
    	"dueling": Dueling,
    	"great-weapon fighting": GreatWeaponFighting,
    	"two-weapon fighting": TwoWeaponFighting,
    }
    name = "Fighting Style (Select One)"
    source = "Blood Hunter"


class CrimsonRites(Feature):
    """At 2nd level, you learn to invoke a rite of hemocraft within your weapon at the cost of your own vitality. Choose one rite from the Primal Rites list below to learn.

As a bonus action, you can activate a crimson rite on a single weapon with the elemental energy of a known rite of your choice that lasts until you finish a short or long rest, or if you aren’t holding the weapon at the end of your turn. When you activate a rite, you lose a number of hit points equal to one roll of your hemocraft die, as shown in the Hemocraft Die column of the Blood Hunter table.

For the duration, attacks from this weapon deal an additional 1d4 damage of the chosen rite’s type. This damage is magical, and increases as you gain levels as a blood hunter, as shown in the Hemocraft Die column of the Blood Hunter table. A weapon can only hold a single active rite at a time.

You learn an additional Primal Rite at 7th level, and access to an Esoteric Rite at 14th level.
   
    """
    
    name = "Crimson Rites"
    source = "Blood Hunter"


class ExtraAttackBloodHunter(Feature):
    """Beginning at 5th level, you can attack twice, instead of once, whenever you
    take the Attack action on your turn.

    """

    name = "Extra Attack (2x)"
    source = "Blood Hunter"


class BrandOfCastigation(Feature):
    """At 6th level, whenever you damage a creature with your Crimson Rite feature, you can choose to sear an arcane brand of hemocraft magic into it (requires no action). You always know the direction to the branded creature, and each time the branded creature deals damage to you or a creature you can see within 5 feet of you, the creature takes psychic damage equal to your Intelligence modifier (minimum of 1 damage).

Your brand lasts until you dismiss it, or you apply a brand to another creature. Your brand counts as a spell for the purposes of dispel magic, and the spell level is equal to half of your blood hunter level (maximum of 9th level spell).

Once you use this feature, you can’t use it again until you finish a short or long rest.
    
    """


class GrimPsychometry(Feature):
    """When you reach 9th level, you have a supernatural talent for discerning the history surrounding mysterious objects or places touched by evil. When making an Intelligence (History) check to recall information about a darker past surrounding an object you are touching, or a location you are present in, you have advantage on the roll. The information gleaned often leans towards the more sinister influences of the past, and sometimes conveys visions of things previously unknown to the character on higher rolls.
    
    """

    name = "Grim Psychometry"
    source = "Blood Hunter"


class DarkAugmentation(Feature):
    """Upon reaching 10th level, arcane blood magic suffuses your body, permanently reinforcing your resilience. Your speed increases by 5 feet, and whenever you make a Strength, Dexterity, or Constitution saving throw, you gain a bonus to the saving throw equal to your Intelligence modifier (minimum of +1).
    
    """

    name = "Dark Augmentation"
    source = "Blood Hunter"
    
    
class BrandOfTethering(Feature):
    """Starting at 13th level, the psychic damage from your Brand of Castigation increases to twice your Intelligence modifier (minimum of 2 damage).

In addition, a branded creature can’t take the Dash action, and if a creature branded by you attempts to teleport or leave their current plane via ability, spell, or portal, they take 4d6 psychic damage and must make a Wisdom saving throw. On a failure, the teleport or plane shift fails.
    
    """
    
    name = "Brand of Thethering"
    source = "Blood Hunter"
    

class HardenedSoul(Feature):
    """When you reach 14th level, you have advantage on saving throws against being charmed and frightened.
    
    """
    
    name = "Hardened Soul"
    source = "Blood Hunter"


class SanguineMastery(Feature):
    """Upon becoming 20th level, you hone your control over blood magic, mitigating your sacrifice and empowering your capability. Once per turn, whenever a blood hunter feature requires you to roll a hemocraft die, you can choose to reroll the die and choose which result to use.

In addition, whenever you score a critical hit with a weapon attack empowered by your Crimson Rite, you regain one expended use of your Blood Maledict feature.
    
    """
    
    name = "Sanguine Mastery"
    source = "Blood Hunter"
    
    
# All Rites
class Rites(Feature):
    """
    A generic Rite. Add details in features/bloodhunter.py
    """

    name = "Unnamed rite"
    source = "BloodHunter (Crimson Rites)"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if "M" in s.components:
            c = list(s.components)
            c.remove("M")
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self, owner):
        super().__init__(owner)
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)


class RiteOfTheFlame(Rites):
    """Your rite damage is fire damage.
    
    """
    
    name = "Rite of the Flame"


class RiteOfTheFrozen(Rites):
    """Your rite damage is cold damage.

    """
    
    name = "Rite of the Frozen"
    
class RiteOfTheStorm(Rites):
    """Your rite damage is lightning damage.
    
    """    
    
    name = "Rite of the Storm"
    

class RiteOfTheDead(Rites):
    """Your rite damage is necrotic damage
    
    **Prerequisite: 14th level**
    
    """
    
    name = "Rite of the Dead"
    

class RiteOfTheOracle(Rites):
    """Your rite damage is psychic damage
    
    **prerequisite: 14th level**
    
    """
    
    name = "Rite of the Oracle"


class RiteOfTheRoar(Rites):
    """Your rite damage is thunder damage
    
    **Prerequisite: 14th level**
    
    """
    
    name = "Rite of the Roar"
    

#Blood Curses
class BloodCurses(Feature):
    """
    A generic BloodCurse. Add details in features/bloodhunter.py
    """

    name = "Unnamed Curse"
    source = "BloodHunter (Blood Maledict)"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if "M" in s.components:
            c = list(s.components)
            c.remove("M")
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self, owner):
        super().__init__(owner)
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)


class BloodCurseoftheAnxious(BloodCurses):
    """As a bonus action, you magnify the adrenaline in the body of a creature within 30 feet of you, making them susceptible to forceful influence. Until the end of your next turn, all creatures have advantage on Charisma (Intimidation) checks directed at the target creature.

Amplify. The next Wisdom saving throw the target makes before this curse ends has disadvantage. Once you’ve amplified this blood curse, you must finish a long rest before you can amplify it again.
    
    """
    
    name = "Blood Curse of the Anxious"
    
    
class BloodCurseofBinding(BloodCurses):
    """As a bonus action, you can attempt to bind a creature you can see within 30 feet of you that is no more than one size larger than you. The target must succeed on a Strength saving throw or have their speed be reduced to 0 and they can’t use reactions until the end of your next turn.

Amplify. This curse lasts for 1 minute and can affect a creature regardless of their size. At the end of each of its turns, the cursed creature can make another Strength saving throw. On a success, this curse ends.
    
    """
    
    name = "Blood Curse of Binding"    


class BloodCurseOfBloatedAgony(BloodCurses):
    """As a bonus action, you curse a creature that you can see within 30 feet of you to painfully swell until the end of your next turn. For the duration of this curse, the creature has disadvantage on Strength and Dexterity ability checks, and suffers 1d8 necrotic damage if it makes more than one melee or ranged attack during its turn.

Amplify. This curse lasts for 1 minute. At the end of each of its turns, the cursed creature can make a Constitution saving throw. On a success, this curse ends.
    
    """
    
    name = "Blood Curse of Bloated Agony"


class BloodCurseOfCorrosion(BloodCurses):
    """**Prerequisite: 15th level, Order of the Mutant**

As a bonus action, a creature within 30 feet of you becomes poisoned. At the end of each of its turns, the target can make another Constitution saving throw. On a success, the curse ends.

Amplify. The cursed creature suffers 4d6 necrotic damage, and suffers this damage again every time it fails its Constitution saving throw to end this curse at the end of its turn.
    
    """
    
    name = "Blood Curse of Corrosion"


class BloodCurseOfTheExorcist(BloodCurses):
    """**Prerequisite: 15th level, Order of the Ghostslayer**

As a bonus action, you can choose one creature you can see within 30 feet of you that is charmed, frightened, or possessed. The target creature is no longer charmed, frightened, or possessed.

Amplify. The creature that charmed, frightened, or possessed the target of your curse suffers 3d6 psychic damage and must make a Wisdom saving throw or be stunned until the end of your next turn.
    
    """
    
    name = "Blood Curse of the Exorcist"


class BloodCurseOfExposure(BloodCurses):
    """When a creature you can see within 30 feet is hit by an attack or spell, you can use your reaction to temporarily weaken their resilience against it. Until the end of the turn, the target loses resistance to the damage types of the triggering attack or spell.

Amplify. The target instead loses invulnerability to the damage types of the triggering attack or spell, having resistance to them until the end of the turn.
    
    """
    
    name = "Blood Curse of Exposure"
    

class BloodCurseOfTheEyeless(BloodCurses):
    """When a creature you can see within 30 feet of you makes an attack roll, you can use your reaction to roll one hemocraft die and subtract the number rolled from the creature’s attack roll. You can choose to use this feature after the creature’s roll, but before the DM determines whether the attack roll succeeds. The creature is immune if it is immune to blindness.

Amplify. You apply this curse to all of the creature’s attack rolls until the end of the turn. You roll a new hemocraft die for each affected attack.
    
    """
    
    name = "Blood Curse of Exposure"
    

class BloodCurseOfTheFallenPuppet(BloodCurses):
    """When a creature you can see within 30 feet of you drops to 0 hit points, you can use your reaction to give that creature a final act of aggression. That creature immediately makes a single weapon attack against a target of your choice within its attack range.

Amplify. You can first move the cursed creature up to half their speed, and you grant a bonus to the cursed creature’s attack roll equal to your Intelligence modifier (minimum of +1).
    
    """
    
    name = "Blood Curse of the Fallen Puppet"
    

class VloodCurseOfTheHowl(BloodCurses):
    """**Prerequisite: 18th level, Order of the Lycan**

As an action, you unleash a blood-curdling howl. Each creature within 30 feet of you that can hear you must succeed on a Wisdom saving throw or become frightened of you until the end of your next turn. If they fail their saving throw by 5 or more, they are stunned while frightened in this way. A creature that succeeds on this saving throw is immune to this blood curse for the next 24 hours.

You can choose any number of creatures you can see to be unaffected by the howl.

Amplify. The range of this curse increases to 60 feet.
    
    """
    
    name = "Blood Curse of the Howl"


class BloodCurseOfTheMarked(BloodCurses):
    """As a bonus action, you can mark a creature that you can see within 30 feet of you. Until the end of your turn, whenever you deal rite damage to the target, you roll an additional hemocraft die of rite damage.

Amplify. The next attack roll you make against the target before the end of your turn has advantage.
    
    """
    
    name = "Blood Curse of the Marked"
    

class BloodCurseOfTheMuddledMind(BloodCurses):
    """As a bonus action, you curse a creature that you can see within 30 feet of you that is concentrating on a spell. That creature has disadvantage on the next Constitution saving throw it must make to maintain concentration before the end of your next turn.

Amplify. The cursed creature has disadvantage on all Constitution saving throws made to maintain concentration of spells until the end of your next turn.
    
    """    
    
    name = "Blood Curse of the Muddled Mind"


class BloodCurseOfTheSouleater(BloodCurses):
    """**Prerequisite: 18th level, Order of the Profane Soul**

When a creature that isn’t a construct or undead is reduced to 0 hit points within 30 feet of you, you can use your reaction to usher their soul to your patron in exchange for power. Until the end of your next turn, your weapon attacks have advantage.

Amplify. In addition, you regain an expended warlock spell slot. Once you’ve amplified this blood curse, you must finish a long rest before you can amplify it again
    
    """    
    
    name = "Blood Curse of the Souleater"


#Order of the Ghostslayer
class CurseSpecialist(Feature):
    """Beginning at 3rd level, your ancient order teaches advanced mastery over blood curses. You gain an additional use of your Blood Maledict feature. In addition, your blood curses can target any creature, whether it has blood or not.
    
    """
    
    name = "Curse Specialist"
    source = "Blood Hunter (Order of the Ghostslayer)"


class RiteOfTheDawn(Rites):
    """When you join this order at 3rd level, you learn the Rite of the Dawn esoteric rite (detailed below).

Rite of the Dawn. Your rite damage is radiant damage. While the rite is active, you gain the following benefits:

    Your weapon sheds bright light out to a radius of 20 feet.
    You have resistance to necrotic damage.
    Your weapon deals one additional hemocraft die of rite damage when you hit an undead

    """
    
    name = "Rite of the Dawn"
    source = "Blood Hunter (Order of the Ghostslayer)"


class EtherealStep(Feature):
    """Upon reaching 7th level, at the start of your turn, if you aren’t incapacitated, you can choose to magically step into the veil between the planes.

You can move through other creatures and objects as if they were difficult terrain, as well as see and affect creatures and objects on the Ethereal Plane. You take 1d10 force damage if you end your turn inside an object. If you are inside an object when this feature ends, you are immediately shunted to the nearest unoccupied space that you can occupy and take force damage equal to twice the number of feet you moved. This feature lasts for a number of rounds equal to your Intelligence modifier (minimum of 1 round).

You can use this feature once. Beginning at 15th level, you can use your Ethereal Step feature twice between rests. You regain all expended uses when you finish a short or long rest.
    
    """
    
    name = "Ethereal Step"
    source = "Blood Hunter (Order of the Ghostslayer)"
    
    
class BrandOfSundering(Feature):
    """Beginning at 11th level, your Brand of Castigation now exposes a fragment of your foe’s essence, leaving them vulnerable to your Crimson Rite. Whenever you damage a branded creature with your Crimson Rite, your weapon deals one additional hemocraft die of rite damage. In addition, the branded creature can’t move through creatures or objects.
    
    """
    
    name = "Brand of Sundering"
    source = "Blood HUnter (Order of the Ghostslayer)"
    
    
class BloodCurseOfTheExorcist(Feature):
    """At 15th level, you’ve honed your hemocraft to tear wicked influence from your allies, punishing those who would infiltrate their body and mind. You gain the Blood Curse of the Exorcist for your Blood Maledict feature. This doesn’t count against your number of blood curses known.
    
    """
    
    name = "Blood Curse of the Exorcist"
    source = "Blood Hunter (Order of the Ghostslayer"
    
    
class RiteRevival(Feature):
    """Upon reaching 18th level, you learn to protect your fading life by absorbing your blood rite. When you are reduced to 0 hit points while you have an active Crimson Rite, but don’t die outright, the rite ends and you drop to 1 hit point instead. If you have rites active on multiple weapons, you choose which one ends.
    
    """
    
    name = "Revival"
    source = "Blood Hunter (Order of the Ghostslayer)"
    
    
#Order of the Lycan
class HeightenedSenses(Feature):
    """Starting when you choose this archetype at 3rd level, you begin to adopt the improved abilities of a natural predator. You gain advantage on Wisdom (Perception) checks that rely on hearing or smell.
    
    """
    
    name = "Revival"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class HybridTransformation(Feature):
    """Upon choosing this archetype at 3rd level, you begin to learn to control the lycanthropic curse that now lives in your blood. As a bonus action, you can transform into your hybrid form for up to 1 hour. You can speak, use equipment, and wear armor in this form. You can revert to your normal form earlier as a bonus action. You automatically revert to your normal form if you fall unconscious, drop to 0 hit points, or die. This feature replaces the rules for Lycanthropy within the Monster’s Manual.

Once you use this feature, you must finish a short or long rest before you can use it again.

While you are transformed, you gain the following features:

Feral Might. You gain a +1 to melee damage rolls. This bonus increases by 1 at 11th and 18th level. You also have advantage on Strength checks and Strength saving throws.

Resilient Hide. You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks not made with silver weapons. While you are not wearing heavy armor, you gain a +1 bonus to your AC.

Predatory Strikes. You can apply your Crimson Rite feature to your unarmed strikes as a single weapon. You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes. When you use the Attack action with an unarmed strike, you can make one unarmed strike as a bonus action.

Your unarmed strikes deal 1d6 slashing damage. The damage increases to 1d8 at 11th level.

Bloodlust. If you begin your turn with no more than half of your maximum hit points, you must succeed on a DC 8 Wisdom saving throw or move directly towards the nearest creature to you and use the Attack action against that creature. You can choose whether or not to use your Extra Attack feature for this frenzied attack. If there is more than one possible target, roll to randomly determine the target. You then regain control for the remainder of your turn.

If you are under an effect that prevents you from concentrating (like the barbarian’s Rage feature), you automatically fail this saving throw.
    
    """
    
    name = "Hybrid Transformation"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class StalkerProwess(Feature):
    """At 7th level, your speed increases by 10 feet. You also can add 10 feet to your long jump distance and 3 feet to your high jump distance. In addition, your hybrid form gains the Improved Predatory Strikes feature.

Improved Predatory Strikes. You gain a +1 bonus to attack rolls made with your unarmed strikes. This bonus increases by 1 at 11th level (+2) and 18th level (+3). In addition, when you have an active Crimson Rite while in your hybrid form, your unarmed strikes are considered magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.
    
    """
    
    name = "Stalker Prowess"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class AdvancedTrasformation(Feature):
    """Starting at 11th level, you learn to unleash and control more of the beast within. You can use your Hybrid Transformation feature twice, regaining all expended uses when you finish a short or long rest. In addition, your hybrid form gains the Lycan Regeneration feature.

Lycan Regeneration. At the start of each of your turns, before you roll for bloodlust, you regain hit points equal to 1 + your Constitution modifier (minimum of one) if you have at least 1 hit point and no more than half of your hit points left.
    
    """
    
    name = "Advanced Transformation"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class BrandOfTheVoracious(Feature):
    """At 15th level, you have advantage on your Wisdom saving throws to maintain control of your bloodlust in hybrid form. In addition, your Brand of Castigation now binds your foe to your hunter’s thirst for savagery. While in your hybrid form, your attacks have advantage against a creature branded by you.
    
    """
    
    name = "Brand of the Voracious"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class HybridTrasformationMastery(Feature):
    """At 18th level, you have wrestled your inner predator and mastered it. You can use your Hybrid Transformation feature an unlimited number of times, and your hybrid form can now last indefinitely.

You also gain the Blood Curse of the Howl for your Blood Maledict feature. This does not count against your number of blood curses known.
    
    """
    
    name = "Hybrid Transformation Mastery"
    source = "Blood Hunter (Order of the Lycan)"
    

#Order of the Mutant
class Formulas(Feature):
    """You begin to uncover forbidden alchemical formulas that temporarily alter your mental and physical abilities.

Beginning at 3rd level, you choose to learn four mutagen formulas. Your formula options are detailed at the end of this order description. You gain an additional formula at 7th level, 11th level, 15th level, and 18th level.

Additionally, when you gain a new mutagen formula, you can choose one of the formulas you already know and replace it with a new mutagen formula.
    
    """
    
    name = "Formulas"
    source = "Blood Hunter (Order of the Mutant)"
    
    
class Mutagencraft(Feature):
    """At 3rd level, you can concoct a single mutagen when you finish a short or long rest. Starting at 7th level, the number of mutagens you can create when you finish a rest increases to two, and at 15th level, you can now create three mutagens.

As a bonus action you can consume a single mutagen, and the effects and side effects last until you finish a short or long rest, unless otherwise specified. While one or more mutagens are affecting you, you can use an action to focus and flush the toxins from your system, ending the effects and side effects of all mutagens.

Mutagens are designed for your biology and have no effect on other creatures. They are also unstable by nature, losing their potency over time and becoming inert if not used before you finish your next short or long rest.
    
    """
    
    name = "Mutagencraft"
    source = "Blood Hunter (Order of the Mutant)"
    
    
class StrangeMetabolism(Feature):
    """Beginning at 7th level, your body has begun to adapt to toxins and venoms, ignoring their corroding effects. You gain immunity to poison damage and the poisoned condition.

In addition, you can instill a burst of adrenaline to temporarily resist the negative effects of a mutagen. As a bonus action, you can choose to ignore the side effect of a mutagen affecting you for 1 minute.

Once you use this feature to resist side effects, you can’t do so again until you finish a long rest.
    
    """
    
    name = "Strange Metabolism"
    source = "Blood Hunter (Order of the Mutant)"


class BrandOfAxiom(Feature):
    """At 11th level, your hemocraft has altered your Brand of Castigation to enforce a foe’s true nature. Any illusions disguising or making a creature invisible when you brand them end, and they can’t benefit from such illusions while branded. If a creature branded by you is polymorphed or has changed shape, they must succeed on a Wisdom saving throw or revert to their true form and be stunned until the end of your next turn. Whenever a branded creature attempts to polymorph or change shape, they must succeed on a Wisdom saving throw or the attempt fails, and they are stunned until the end of your next turn.
    
    """
    
    name = "Brand of Axiom"
    source = "Blood Hunter (Order of the Mutant)"
    
    
class BloodCurseOfCorrosion(Feature):
    """Starting at 15th level, your blood curse can wrack a creature’s body with terrible toxins. You gain the Blood Curse of Corrosion for your Blood Maledict feature. This does not count against your number of blood curses known.
    
    """
    
    name = "Blood Curse of Corrosion"
    source = "Blood Hunter (Order of the Mutant)"
    
    
class ExaltedMutation(Feature):
    """At 18th level, your body has adapted to produce your toxins naturally in a moment of need. As a bonus action, you can choose one mutagen currently affecting you to flush from your system and end, then immediately have a mutagen you know the formula for take effect in its place.

You can use this feature a number of times equal to your Intelligence modifier (minimum of 1). You regain all uses of this feature after you finish a long rest.
    
    """
    
    name = "Exalted Mutation"
    source = "Blood Hunter (Order of the Mutant)"
    
    
#Formulas
class Formulas(Feature):
    """
    A generic Formula. Add details in features/bloodhunter.py
    """

    name = "Unnamed rite"
    source = "BloodHunter (Crimson Rites)"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if "M" in s.components:
            c = list(s.components)
            c.remove("M")
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self, owner):
        super().__init__(owner)
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)
            
            
class Aether(Formulas):
    """**Prerequisite: 11th level.**
You gain a flying speed of 20 feet for 1 hour.
Side effect. You have disadvantage on Strength and Dexterity ability checks for 1 hour.
    
    """
    
    name = "Aether"
    

class Alluring(Formulas):
    """Your skin and voice become malleable, allowing you to slightly enhance your appearance and presence. You have advantage on Charisma ability checks.
Side effect. You have disadvantage on initiative rolls.
    
    """
    
    name = "Alluring"
    
    
class Celerity(Formulas):
    """Your Dexterity score increases by 3, as does your Dexterity maximum. This bonus increases by 1 at 11th and 18th level.
Side effect. You have disadvantage on Wisdom saving throws.
    
    """
    
    name = "Celerity"
    

class Conversant(Formulas):
    """You gain advantage on Intelligence ability checks.
Side effect. You have disadvantage on Wisdom ability checks.
    
    """
    
    name = "Conversant"
    
    
class Cruelty(Formulas):
    """**Prerequisite: 11th level.**
When you use the Attack action, you can make an additional weapon attack as a bonus action.
Side effect. You have disadvantage on Intelligence, Wisdom, and Charisma saving throws.
    
    """
    
    name = "Cruelty"
    
    
class Deftness(Formulas):
    """You gain advantage on Dexterity ability checks.
Side effect. You have disadvantage on Wisdom ability checks.
    
    """
    
    name = "Deftness"
    
    
class Embers(Formulas):
    """You gain resistance to fire damage.
Side effect. You gain vulnerability to cold damage.
    
    """
    
    name = "Embers"
    
    
class Gelid(Formulas):
    """You gain resistance to cold damage.
Side effect. You gain vulnerability to fire damage.

    """
    
    name = "Gelid"
    
    
class Impermeable(Formulas):
    """You gain resistance to piercing damage.
Side effect. You gain vulnerability to slashing damage.
    
    """
    
    name = "Impermeable"
    
    
class Mobility(Formulas):
    """You gain immunity to the grappled and restrained conditions. At 11th level, you also are immune to the paralyzed condition.
Side effect. You have disadvantage on Strength ability checks.
    
    """
    
    name = "Mobility"
    
    
class Nighteye(Formulas):
    """You gain darkvision for up to 60 feet. If you already have darkvision, this increases its range by 60 additional feet.
Side effect. You gain sunlight sensitivity (detailed in the Dark Elf section of the Player’s Handbook).
    
    """
    
    name = "Nighteye"
    
    
class Percipient(Formulas):
    """You gain advantage on Wisdom ability checks.
Side effect. You have disadvantage on Charisma ability checks.
    
    """
    
    name = "Percipient"
    
    
class Potency(Formulas):
    """Your Strength score increases by 3, as does your Strength maximum. This bonus increases by 1 at 11th and 18th level.
Side effect. You have disadvantage on Dexterity saving throws.
    
    """
    
    name = "Potency"
    
    
class Precision(Formulas):
    """**Prerequisite: 11th level**
Your weapon attacks score a critical hit on a roll of 19-20.
Side effect. You have disadvantage on Strength saving throws.
    
    """
    
    name = "Precision"
    

class Rapidity(Formulas):
    """Your speed increases by 10 feet. At 15th level, your speed increases by 15 feet instead.
Side effect. You have disadvantage on Intelligence ability checks.
    
    """
    
    name = "Rapidity"
    
    
class Reconstruction(Formulas):
    """**Prerequisite: 7th level**
For 1 hour, at the start of each of your turns, you regain hit points equal to your proficiency bonus if you have at least 1 hit point, but no more than half of your hit points.
Side effect. Your speed decreases by 10 ft for 1 hour.
    
    """
    
    name = "Reconstruction"
    
    
class Sagacity(Formulas):
    """Your Intelligence score increases by 3, as does your Intelligence maximum. This bonus increases by 1 at 11th and 18th level.
Side effect. You have disadvantage on Charisma saving throws.
    
    """
    
    name = "Sagacity"
    
    
class Shielded(Formulas):
    """You gain resistance to slashing damage.
Side effect. You gain vulnerability to bludgeoning damage.
    
    """
    
    name = "Shielded"
    
    
class Unbreakable(Formulas):
    """You gain resistance to bludgeoning damage.
Side effect. You gain vulnerability to piercing damage.

    """
    
    name = "Unbreakable"
    
    
class Vermillion(Formulas):
    """You gain an additional use of your Blood Maledict feature.
Side effect. You have disadvantage on death saving throws.
    
    """
    
    name = "Vermillion"
    

#Order of the Profane Soul
class ArchfeyPatron(Feature):
    """When you deal rite damage to a creature, it glows with faint light until the end of your next turn. For the duration, the creature can’t benefit from half cover, three-quarters cover, or being invisible.
    
    """
    
    name = "Archfey Patron"
    source = "Blood Hunter (Order of the Profane Soul)"


class CelestialPatron(Feature):
    """You can expend a use of your Blood Maledict feature as a bonus action to heal one creature that you can see within 60 feet of you. They regain a number of hit points hit points equal to one roll of your hemocraft die + your Intelligence modifier (minimum of +1).
    
    """
    
    name = "Celestial Patron"
    source = "Blood Hunter (Order of the Profane Soul) "
    
    
class FiendPatron(Feature):
    """While using the Rite of the Flame, if you roll a 1 or 2 on your rite damage die, you can reroll the die and choose which roll to use.
    
    """
    
    name = "Fiend Patron"
    source = "Blood Hunter (Order of the Profane Soul)"


class GreatOldOnePatron(Feature):
    """When you score a critical hit against a creature while using the weapon, that creature is frightened of you until the end of your next turn.
    
    """
    
    name = "Great Old One Patron"
    source = "Blood Hunter (Order of the Profane Soul) "


class HexbladePatron(Feature):
    """Whenever you target a creature with a blood curse, your next attack against the cursed creature deals additional damage equal to your proficiency modifier.
    
    """
    
    name = "Hexblade Patron"
    source = "Blood Hunter (Order of the Profane Soul)"


class UndyingPatron(Feature):
    """Whenever you reduce a hostile creature to 0 hit points using a weapon attack, you regain a number of hit points equal to one roll of your hemocraft die.
    
    """
    
    name = "Undying Patron"
    source = "Blood Hunter (Order of the Profane Soul)"


class OtherworldlyPatron(FeatureSelector):
    """When you reach 3rd level, you strike a bargain with an otherworldly being of your choice: the Archfey, the Fiend, or the Great Old One, each detailed in the Player’s Handbook, the Undying within the Sword Coast Adventurer’s Guide, and the Celestial or Hexblade in Xanathar’s Guide to Everything. Your choice augments some of your order features.
    
    """
    
    options = {
    	"Archfey": ArchfeyPatron,
    	"Celestial": CelestialPatron,
    	"Fiend": FiendPatron,
    	"Great Old One": GreatOldOnePatron,
    	"Hexblade": HexbladePatron,
    	"Undying": UndyingPatron,
    }
    name = "Otherworldly Patron (Select One)"
    source = "Blood Hunter (Order of the Profane Soul)"
    

class PactMagic(Feature):
    """When you reach 3rd level, you can augment your combat techniques with the ability to cast spells. See chapter 10 of the PHB for the general rules of spellcasting and chapter 11 of the Player’s Handbook for the Warlock spell list.

Cantrips. You learn two cantrips of your choice from the warlock spell list. You learn an additional warlock cantrip of your choice at 10th level.

Spell Slots. The Profane Soul Spellcasting table shows how many spell slots you have. The table also shows what the level of those slots is; all of your spell slots are the same level. To cast one of your warlock spells of 1st level or higher, you must expend a spell slot. You regain all expended spell slots when you finish a short or long rest.

For example, when you are 8th level, you have two 2nd-level spell slots. To cast the 1st-level spell witch bolt, you must spend one of those slots, and you cast it as a 2nd-level spell.

Spells Known of 1st Level and Higher. At 3rd level, you know two 1st-level spells of your choice from the warlock spell list.

The Spells Known column of the Profane Soul table shows when you learn more warlock spells of your choice of 1st level and higher. A spell you choose must be of a level no higher than what’s shown in the table’s Slot Level column for your level. When you reach 11th level, for example, you learn a new warlock spell, which can be 1st, 2nd, or 3rd level.

Additionally, when you gain a level in this class and order, you can choose one of the warlock spells you know and replace it with another spell from the warlock spell list, which also must be of a level for which you have spell slots.

Spellcasting Ability. Intelligence is your spellcasting ability for your warlock spells, so you use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a warlock spell you cast and when making an attack roll with one.

Spell save DC = 8 + your proficiency bonus + your Intelligence modifier

Spell attack modifier = your proficiency bonus + your Intelligence modifier
    
    """
    
    name = "Pact Magic"
    source = "Blood Hunter (Order of the Profane Soul)"


class RiteFocus(Feature):
    """Beginning at 3rd level, your weapon becomes a core to your pact with your chosen dark patron. While you have an active Crimson Rite, you can use your weapon as a spellcasting focus (found in chapter 5 of the Player’s Handbook) for your warlock spells, and you gain a specific benefit based on your chosen pact (outlined below).
    
    The Archfey

When you deal rite damage to a creature, it glows with faint light until the end of your next turn. For the duration, the creature can’t benefit from half cover, three-quarters cover, or being invisible.

The Celestial

You can expend a use of your Blood Maledict feature as a bonus action to heal one creature that you can see within 60 feet of you. They regain a number of hit points hit points equal to one roll of your hemocraft die + your Intelligence modifier (minimum of +1).

The Fiend

While using the Rite of the Flame, if you roll a 1 or 2 on your rite damage die, you can reroll the die and choose which roll to use.

The Great Old One

When you score a critical hit against a creature while using the weapon, that creature is frightened of you until the end of your next turn.

The Hexblade

Whenever you target a creature with a blood curse, your next attack against the cursed creature deals additional damage equal to your proficiency modifier.

The Undying

Whenever you reduce a hostile creature to 0 hit points using a weapon attack, you regain a number of hit points equal to one roll of your hemocraft die.

    """
    
    name = "Rite Focus"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class MysticFrenzy(Feature):
    """Starting at 7th level, when you use your action to cast a cantrip, you can immediately make one weapon attack as a bonus action.
    
    """
    
    name = "Mystic Frenzy"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class RevealedArcana(Feature):
    """At 7th level, your dark patron grants you the rare use of a dangerous arcane spell based on your pact.
The Archfey

You can cast blur once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Celestial

You can cast lesser restoration once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Fiend

You can cast scorching ray once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Great Old One

You can cast detect thoughts once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Hexblade

You can cast branding smite once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Undying

You can cast blindness/deafness once using a pact magic spell slot. You can’t do so again until you finish a long rest.
    
    """
    
    name = "Revealed Arcana"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class BrandOfTheSappingScar(Feature):
    """Upon reaching 11th level, your Brand of Castigation feature now digs dark, arcane scars into your target, leaving them vulnerable to your magic. A creature branded by you has disadvantage on their saving throws against your warlock spells.
    
    """
    
    name = "Brand of the Sapping Scar"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class UnsealedArcana(Feature):
    """At 15th level, your patron grants you the rare use of an additional arcane spell based on your pact.
The Archfey

You can cast slow once without expending a spell slot. You can’t do so again until you finish a long rest.

The Celestial

You can cast revivify once without expending a spell slot. You can’t do so again until you finish a long rest.

The Fiend

You can cast fireball once without expending a spell slot. You can’t do so again until you finish a long rest.

The Great Old One

You can cast haste once without expending a spell slot. You can’t do so again until you finish a long rest.

The Hexblade

You can cast blink once without expending a spell slot. You can’t do so again until you finish a long rest.

The Undying

You can cast bestow curse once without expending a spell slot. You can’t do so again until you finish a long rest.
    
    """
    
    name = "Brand of the Sapping Scar"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class BloodCurseOfTheSouleater(Feature):
    """Starting at 18th level, you’ve learned to siphon the soul from your fallen prey. You gain the Blood Curse of the Souleater for your Blood Maledict feature. This does not count against your number of blood curses known.
    
    """
    
    name = "Brand of the Sapping Scar"
    source = "Blood Hunter (Order of the Profane Soul)"
