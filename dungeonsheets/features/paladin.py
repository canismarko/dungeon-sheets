from dungeonsheets.features.features import Feature, FeatureSelector
from dungeonsheets.features.fighter import GreatWeaponFighting, Protection
from dungeonsheets.features.ranger import Defense, Dueling


# PHB
class DivineSense(Feature):
    """The presence of strong evil registers on your senses like a noxious odor,
    and powerful good rings like heavenly music in your ears. As an action, you
    can open your awareness to detect such forces. Until the end of your next
    turn, you know the location of any celestial, fiend, or undead within 60
    feet of you that is not behind total cover. You know the type (celestial,
    fiend, or undead) of any being whose presence you sense, but not its
    identity (the vampire Count Strahd von Zarovich, for instance). Within the
    same radius, you also detect the presence of any place or object that has
    been consecrated or desecrated, as with the hallow spell.

    You can use this feature a number of times equal to 1 + your Charisma
    modifier. When you finish a long rest, you regain all expended uses.

    """

    _name = "Divine Sense"
    source = "Paladin"

    @property
    def name(self):
        num_uses = max(1, 1 + self.owner.charisma.modifier)
        return self._name + " ({:d}x/LR)".format(num_uses)


class LayOnHands(Feature):
    """Your blessed touch can heal wounds. You have a pool of healing power that
    replenishes when you take a long rest. With that pool, you can restore a
    total number of hit points equal to your paladin level x 5.

    As an action, you can touch a creature and draw power from the pool to
    restore a number of hit points to that creature, up to the maximum amount
    remaining in your pool.

    Alternatively, you can expend 5 hit points from your pool of healing to
    cure the target of one disease or neutralize one poison affecting it. You
    can cure multiple diseases and neutralize multiple poisons with a single
    use of Lay on Hands, expending hit points separately for each one.

    This feature has no effect on undead and constructs

    """

    _name = "Lay on Hands"
    source = "Paladin"

    @property
    def name(self):
        level = self.owner.Paladin.level
        return self._name + " ({:d}HP/LR)".format(level * 5)


class PaladinFightingStyle(FeatureSelector):
    """
    Select a Fighting Style by choosing in feature_choices:

    defense

    dueling

    great-weapon fighting

    protection
    """

    options = {
        "defense": Defense,
        "dueling": Dueling,
        "great": GreatWeaponFighting,
        "great-weapon fighting": GreatWeaponFighting,
        "projection": Protection,
    }
    name = "Fighting Style (Select One)"
    source = "Paladin"


class DivineSmite(Feature):
    """Starting at 2nd level, when you hit a creature with a melee weapon attack,
    you can expend one paladin spell slot to deal radiant damage to the target,
    in addition to the weapon's damage. The extra damage is 2d8 for a 1st-level
    spell slot, plus 1d8 for each spell level higher than 1st, to a maximum of
    5d8. The damage increases by 1d8 if the target is an undead or a fiend.

    """

    name = "Divine Smite"
    source = "Paladin"


class DivineHealth(Feature):
    """By 3rd level, the divine magic flowing through you makes you immune to
    disease"""

    name = "Divine Health"
    source = "Paladin"


class ExtraAttackPaladin(Feature):
    """Beginning at 5th level, you can attack twice, instead of once, whenever you
    take the Attack action on your turn

    """

    name = "Extra Attack (2x)"
    source = "Paladin"


class AuraOfProtection(Feature):
    """Starting at 6th level, whenever you or a friendly creature within 10 feet
    of you must make a saving throw, the creature gains a bonus to the saving
    throw equal to your Charisma modifier (with a minimum bonus of +1). You
    must be conscious to grant this bonus.

    At 18th level, the range of this aura increases to 30 feet.

    """

    name = "Aura of Protection"
    source = "Paladin"


class AuraOfCourage(Feature):
    """Starting at 10th level, you and friendly creatures within 10 feet of you
    can't be frightened while you are conscious.

    At 18th level, the range of this aura increases to 30 feet

    """

    name = "Aura of Courage"
    source = "Paladin"


class ImprovedDivineSmite(Feature):
    """By 11th level, you are so suffused with righteous might that all your melee
    weapon strikes carry divine power with them. Whenever you hit a creature
    with a melee weapon, the creature takes an extra 1d8 radiant damage. If you
    also use your Divine Smite with an attack, you add this damage to the extra
    damage of your Divine Smite.

    """

    name = "Improved Divine Smite"
    source = "Paladin"


class CleansingTouch(Feature):
    """Beginning at 14th level, you can use your action to end one spell on
    yourself or on one willing creature that you touch. You can use this
    feature a number of times equal to your Charisma modifier (a minimum of
    once). You regain expended uses when you finish a long rest.

    """

    _name = "Cleansing Touch"
    source = "Paladin"

    @property
    def name(self):
        num_uses = max(1, 1 + self.owner.charisma.modifier)
        return self._name + " ({:d}x/LR)".format(num_uses)


class ChannelDivinityPaladin(Feature):
    """Your oath allows you to channel divine energy to fuel magical effects. Each
    Channel Divinity option provided by your oath explains how to use it.

    When you use your Channel Divinity, you choose which option to use. You
    must then finish a short or long rest to use your Channel Divinity
    again.

    Some Channel Divinity effects require saving throws.  When you use such an
    effect from this class, the DC equals your paladin spell save DC.

    """

    name = "Channel Divinity (1x/SR)"
    source = "Paladin"


# Oath of Devotion
class SacredWeapon(Feature):
    """As an action, you can imbue one weapon that you are holding with positive
    energy, using your Channel Divinity. For 1 minute, you add your Charisma
    modifier to attack rolls made with that weapon (with a minimum bonus of
    +1). The weapon also emits bright light in a 20-foot radius and dim light
    20 feet beyond that. If the weapon is not already magical, it becomes
    magical for the duration.

    You can end this effect on your turn as part of any other action. If you
    are no longer holding or carrying this weapon, or if you fall unconscious,
    this effect ends.

    """

    name = "Channel Divinity: Sacred Weapon"
    source = "Paladin (Oath of Devotion)"


class TurnTheUnholy(Feature):
    """As an action, you present your holy symbol and speak a prayer censuring
    fiends and undead, using your Channel Divinity. Each fiend or undead that
    can see or hear you within 30 feet of you must make a W isdom saving
    throw. If the creature fails its saving throw, it is turned for 1 minute or
    until it takes damage.

    A turned creature must spend its turns trying to move as far away from you
    as it can, and it can't willingly move to a space within 30 feet of you. It
    also can't take reactions. For its action, it can use only the Dash action
    or try to escape from an effect that prevents it from moving. If there's
    nowhere to move, the creature can use the Dodge action.

    """

    name = "Channel Divinity: Turn the Unholy"
    source = "Paladin (Oath of Devotion)"


class AuraOfDevotion(Feature):
    """Starting at 7th level, you and friendly creatures within 10 feet of you
    can't be charmed while you are conscious. At 18th level, the range of this
    aura increases to 30 feet.

    """

    name = "Aura of Devotion"
    source = "Paladin (Oath of Devotion)"


class PurityOfSpirit(Feature):
    """Beginning at 15th level, you are always under the effects of a protection
    from evil and good spell.

    """

    name = "Purity of Spirit"
    source = "Paladin (Oath of Devotion)"


class HolyNimbus(Feature):
    """At 20th level, as an action, you can emanate an aura of sunlight. For 1
    minute, bright light shines from you in a 30-foot radius, and dim light
    shines 30 feet beyond that.

    Whenever an enemy creature starts its turn in the bright light, the
    creature takes 10 radiant damage.

    In addition, for the duration, you have advantage on saving throws against
    spells cast by fiends or undead. Once you use this feature, you can't use
    it again until you finish a long rest.

    """

    name = "Holy Nimbus"
    source = "Paladin (Oath of Devotion)"


# Oath of the Ancients
# Oath of Redemption
class EmissaryOfPeace(Feature):
    """You can use your Channel Divinity to augment your presence with divine
    power. As a bonus action, you grant yourself a +5 bonus to Charisma
    (Persuasion) checks for the next 10 minutes.

    """

    name = "Channel Divinity: Emissary of Peace"
    source = "Paladin (Oath of Redemption)"


class RebukeTheViolent(Feature):
    """You can use your Channel Divinity to rebuke those who use
    violence. Immediately after an attacker within 30 feet ofyou deals damage
    with an attack against a creature other than you, you can use your reaction
    to force the attacker to make a Wisdom saving throw. On a failed save, the
    attacker takes radiant damage equal to the damage it just dealt. On a
    successful save, it takes half as much damage.

    """

    name = "Channel Divinity: Rebuke the Violent"
    source = "Paladin (Oath of Redemption)"


class AuraOfTheGuardian(Feature):
    """Starting at 7th level, you can shield others from harm at the cost of your
    own health. When a creature within 10 feet of you takes damage, you can use
    your reaction to magically take that damage, instead of that creature taking
    it. This feature doesn't transfer any other effects that might accompany
    the damage, and this damage can't be reduced in any way. At 18th level,
    the range of this aura increases to 30 feet.

    """

    name = "Aura of the Guardian"
    source = "Paladin (Oath of Redemption)"


class ProtectiveSpirit(Feature):
    """Starting at 15th level, a holy presence mends your wounds in battle. You
    regain hit points equal to 1d6 + half your paladin level if you end your
    turn in combat with fewer than half of your hit points remaining and you
    aren't incapacitated.

    """

    name = "Protective Spirit"
    source = "Paladin (Oath of Redemption)"


class EmissaryOfRedemption(Feature):
    """At 20th level, you become an avatar of peace, which gives you two benefits:

    --You have resistance to all damage dealt by other crea- tures (their
    attacks, spells, and other effects).

    --Whenever a creature hits you with an attack, it takes radiant damage
    equal to half the damage you take from the attack.

    If you attack a creature, cast a spell on it, or deal damage to it by any
    means but this feature, neither benefit works against that creature until
    you finish a long rest

    """

    name = "Emissary of Redemption"
    source = "Paladin (Oath of Redemption)"
