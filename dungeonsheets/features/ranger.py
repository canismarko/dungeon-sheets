from .features import Feature, FeatureSelector
from .. import (weapons, armor)
from .rogue import UncannyDodge, Evasion


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
    """You are particularly familiar with one type of natural environment and are
    adept at traveling and surviving in such regions. Choose one type of
    favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp,
    or the Underdark.  You choose additional favored terrain types at 6th and
    10th

    When you make an Intelligence or Wisdom check related to your favored
    terrain, your proficiency bonus is doubled if you are using a skill that
    you’re proficient in. While traveling for an hour or more in your favored
    terrain, you gain the following benefits:

    -- Difficult terrain doesn’t slow your group’s travel.

    -- Your group can’t become lost except by magical means.
    
    -- Even when you are engaged in another activity while traveling
    (such as foraging, navigating, or tracking), you remain alert to danger. 

    -- If you are traveling alone, you can move stealthily at a normal pace.

    -- When you forage, you find twice as much food as you normally would.

    -- While tracking other creatures, you also learn their exact number, their
    sizes, and how long ago they passed through the area.

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
        if (isinstance(weapon, weapons.MeleeWeapon)
                and "two-handed" not in weapon.properties.lower()):
            weapon.damage_bonus += 2

    
class TwoWeaponFighting(Feature):
    """When you engage in two-weapon fighting, you can add your ability modifier
    to the damage of the second attack.

    """
    name = "Fighting Style (Two-Weapon Fighting)"
    source = "Ranger"


class RangerFightingStyle(FeatureSelector):
    """
    Select a Fighting Style by choosing in feature_choices:

    archery
 
    defense

    dueling

    two-weapon fighting
    """
    options = {'archery': Archery,
               'defense': Defense,
               'dueling': Dueling,
               'two-weapon fighting': TwoWeaponFighting,
               'two-weapon': TwoWeaponFighting,
               'dual wield': TwoWeaponFighting}
    name = "Fighting Style (Select One)"
    source = "Ranger"


class PrimevalAwareness(Feature):
    """Beginning at 3rd level, you can use your action and expend one ranger spell
    slot to focus your awareness on the region around you. For 1 minute per
    level of the spell slot you expend, you can sense whether the following
    types of creatures are present within 1 mile of you (or within up to 6
    miles if you are in your favored terrain): aberrations, celestials,
    dragons, elementals, fey, fiends, and undead. This feature doesn’t reveal
    the creatures’ location or number.

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
    your turn. Also, you can’t be tracked by nonmagical means, unless you
    choose to leave a trail.

    """
    name = "Vanish"
    source = "Ranger"


class FeralSenses(Feature):
    """At 18th level, you gain preternatural senses that help you fight creatures
    you can’t see. When you attack a creature you can’t see, your inability to
    see it doesn’t impose disadvantage on your attack rolls against it. You are
    also aware of the location of any invisible creature within 30 feet of you,
    provided that the creature isn’t hidden from you and you aren’t blinded or
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
    with a weapon attack, the creature takes an extra 1d8 damage if it’s below
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
    options = {'colossus slayer': ColossusSlayer,
               'giant killer': GiantKiller,
               'horde breaker': HordeBreaker}
    name = "Hunter's Prey (Select One)"
    source = "Ranger (Hunter)"
    

class EscapeTheHorde(Feature):
    """Opportunity attacks against you are made with disadvantage

    """
    name = "Escape the Horde"
    source = "Ranger (Hunter)"


class MultiattackDefense(Feature):
    """When a creature hits you with an attack, you gain a +4 bonus to AC against
    all subsequent attacks made by that creature for the rest of the turn.

    """
    name = "Multiattack Defense"
    source = "Ranger (Hunter)"


class SteelWill(Feature):
    """You have advantage on saving throws against being frightened.

    """
    name = "Steel Will"
    source = "Ranger (Hunter)"


class DefensiveTactics(FeatureSelector):
    """Select a Defensive Tactics option in "feature_choices" in your .py file from
    one of:

    escape the horde

    multiattack defense

    steel will

    """
    options = {'escape the horde': EscapeTheHorde,
               'multiattack defense': MultiattackDefense,
               'steel will': SteelWill}
    name = "Defensive Tactics (Select One)"
    source = "Ranger (Hunter)"


class Volley(Feature):
    """You can use your action to make a ranged attack against any number of
    creatures within 10 feet o f a point you can see within your weapon’s
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
    options = {'volley': Volley,
               'whirlwind attack': WhirlwindAttack}
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
    options = {'evasion': Evasion,
               'stand against of the tide': StandAgainstTheTide,
               'uncanny dodge': UncannyDodge}
    name = "Superior Hunter's Defense (Select One)"
    source = "Ranger (Hunter)"


# Beast Master
class RangersCompanion(Feature):
    """At 3rd level, you gain a beast companion that accompanies you on your
    adventures and is trained to fight alongside you. Choose a beast that is no
    larger than Medium and that has a challenge rating of 1/4 or lower
    (appendix D presents statistics for the hawk, mastiff, and panther as
    examples). Add your proficiency bonus to the beast’s AC, attack rolls, and
    damage rolls, as well as to any saving throws and skills it is proficient
    in. Its hit point maximum equals its normal maximum or four times your
    ranger level, whichever is higher.

    The beast obeys your commands as best as it can. It takes its turn on your
    initiative, though it doesn’t take an action unless you command it to. On
    your turn, you can verbally command the beast where to move (no action
    required by you). You can use your action to verbally command it to take
    the Attack, Dash, Disengage, Dodge, or Help action. Once you have the Extra
    Attack feature, you can make one weapon attack yourself when you command
    the beast to take the Attack action.

    While traveling through your favored terrain with only the beast, you can
    move stealthily at a normal pace. If the beast dies, you can obtain another
    one by spending 8 hours magically bonding with another beast that isn’t
    hostile to you, either the same type of beast as before or a different one.

    """
    name = "Ranger's Companion"
    source = "Ranger (Beast Master)"


class ExceptionalTraining(Feature):
    """Beginning at 7th level, on any of your turns when your beast companion
    doesn’t attack, you can use a bonus action to command the beast to take the
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
    name = 'Dread Ambusher'
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
    """By 7th level, you have honed your ability to resist the mind—altering
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
    against you and doesn’t have advantage on the roll, you can use your
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
    can’t use it again until you finish a short or long rest.

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
    turn. Once you use this feature, you can’t use it again until you finish a
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
    give yourself resistance to all of that attack’s damage on this turn

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
    damage immunities, re— sistances, or vulnerabilities. You can use this
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
    """At 7th level, you gain extra resilience against your prey’s assaults on
    your mind and body. Whenever the target of your Slayer’s Prey forces you to
    make a saving throw and whenever you make an ability check to escape that
    targets grapple, add 1d6 to your roll

    """
    name = "Supernatural Defense"
    source = "Ranger (Monster Slayer)"


class MagicUsersNemesis(Feature):
    """At 11th level, you gain the ability to thwart someone else’s magic. When
    you see a creature casting a spell or teleporting within 60 feet of you,
    you can use your reaction to try to magically foil it. The creature must
    succeed on a Wisdom saving throw against your spell save DC, or its spell
    or teleport fails and is wasted. Once you use this feature, you can’t use
    it again until you finish a short or long rest.

    """
    name = "Magic User's Nemesis"
    source = "Ranger (Monster Slayer)"


class SlayersCounter(Feature):
    """At 15th level, you gain the ability to counterattack when your prey tries
    to sabotage you. If the target of your Slayer’s Prey forces you to make a
    saving throw, you can use your reaction to make one weapon attack against
    the quarry. You make this attack immediately before making the saving
    throw. If your attack hits, your save automatir cally succeeds, in addition
    to the attack’s normal effects

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
    """You are a master of navigating the natural world, and you react with swift
    and decisive action when attacked. This grants you the following benefits:

    --You ignore difficult terrain.

    --You have advantage on initiative rolls.

    --On your first turn during combat, you have advantage on attack rolls
    against creatures that have not yet acted.

    In addition, you are skilled at navigating the wilderness. You gain the
    following benefits when traveling for an hour or more:

    --Difficult terrain doesn’t slow your group’s travel.

    --Your group can’t become lost except by magical means.
    
    --Even when you are engaged in another activity while traveling (such as
    foraging, navigating, or tracking), you remain alert to danger.

    --If you are traveling alone, you can move stealthily at a normal pace.

    --When you forage, you find twice as much food as you normally would.
    
    --While tracking other creatures, you also learn their exact number, their
    sizes, and how long ago they passed through the area.

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
    and the creatures’ general direction and distance (in miles) from you.

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
    benefits of your Companion’s Bond ability. You can have only one animal
    companion at a time.

    If your animal companion is ever slain, the magical bond you share allows
    you to return it to life. With 8 hours of work and the expenditure of 25 gp
    worth of rare herbs and fine food, you call forth your companion’s spirit
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
    class feature, your companion’s abilities also improve. Your companion can
    increase one ability score of your choice by 2, or it can increase two
    ability scores of your choice by 1. As normal, your companion can’t
    increase an ability score above 20 using this feature unless its
    description specifies otherwise.

    Your companion shares your alignment, and has a personality trait and a
    flaw that you can roll for or select from the tables below. Your companion
    shares your ideal, and its bond is always, \“The ranger who travels with me
    is a beloved companion for whom I would gladly give my life.\”

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
     with an attack, it can use its reaction to halve the attack’s damage
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
    you can use your reaction to impose disadvantage on the creature’s attack
    roll against you. You can use this feature before or after the attack roll
    is made, but it must be used before the outcome of the roll is determined

    """
    name = "Stalker's Dodge"
    source = "Revised Ranger (Deep Stalker Conclave)"

