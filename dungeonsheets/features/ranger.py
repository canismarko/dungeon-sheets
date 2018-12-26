from .features import Feature, FeatureSelector
from .. import (weapons, armor)


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
        return weapon

    
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
                and "two-handed" in weapon.properties.lower()):
            weapon.attack_bonus += 2
        return weapon

    
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


class HideInPlainSight(Feature):
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


class Vanish(Feature):
    """Starting at 14th level, you can use the Hide action as a bonus action on
    your turn. Also, you can’t be tracked by nonmagical means, unless you
    choose to leave a trail

    """
    name = "Vanish"
    source = "Revised Ranger"


class FeralSenses(Feature):
    """At 18th level, you gain preternatural senses that help you fight creatures
    you can’t see. When you attack a creature you can’t see, your inability to
    see it doesn’t impose disadvantage on your attack rolls against it.

    You are also aware of the location of any invisible creature within 30 feet
    of you, provided that the creature isn’t hidden from you and you aren’t
    blinded or deafened

    """
    name = "Feral Senses"
    source = "Revised Ranger"


class FoeSlayer(Feature):
    """At 20th level, you become an unparalleled hunter. Once on each of your
    turns, you can add your Wisdom modifier to the attack roll or the damage
    roll of an attack you make. You can choose to use this feature before or
    after the roll, but before any effects of the roll are applied

    """
    name = "Foe Slayer"
    source = "Revised Ranger"


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
