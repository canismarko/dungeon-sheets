from .features import Feature


# Cleric Features
class ChannelDivinity(Feature):
    """At 2nd level, you gain the ability to channel divine energy directly from
    your deity, using that energy to fuel magical effects. You start with two
    such effects: Turn Undead and an effect determined by your domain. Some
    domains grant you additional effects as you advance in levels, as noted in
    the domain description.

    When you use your Channel Divinity, you choose which effect to create. You
    must then finish a short or long rest to use your Channel Divinity again.

    Some Channel Divinity effects require saving throws.  When you use such an
    effect from this class, the DC equals your cleric spell save DC.

    Beginning at 6th level, you can use your Channel Divinity twice between
    rests, and beginning at 18th level you can use it three times between
    rests. When you finish a short or long rest, you regain your expended uses.

    """
    _name = "Channel Divinity"
    source = "Cleric"

    @property
    def name(self):
        level = self.owner.Cleric.level
        if level < 6:
            return "Channel Divinity (1x/SR)"
        elif level < 18:
            return "Channel Divinity (2x/SR)"
        else:
            return "Channel Divinity (3x/SR)"
        

class TurnUndead(Feature):
    """As an action, you present your holy symbol and speak a prayer censuring the
    undead. Each undead that can see or hear you within 30 feet of you must
    make a Wisdom saving throw. If the creature fails its saving throw, it is
    turned for 1 minute or until it takes any damage.

    A turned creature must spend its turns trying to move as far away from you
    as it can, and it can’t willingly move to a space within 30 feet of you. It
    also can’t take reactions. For its action, it can use only the Dash action
    or try to escape from an effect that prevents it from moving. If there’s
    nowhere to move, the creature can use the Dodge action.

    """
    name = "Channel Divinity: Turn Undead"
    source = "Cleric"


class DestroyUndead(Feature):
    """Starting at 5th level, when an undead fails its saving throw against your
    Turn Undead feature, the creature is instantly destroyed if its challenge
    rating is at or below a certain threshold, as shown in the Destroy Undead
    table.

    """
    _name = "Destroy Undead"
    source = "Cleric"

    @property
    def name(self):
        level = self.owner.Cleric.level
        name = self._name + ' (CR 1/2)'
        if level >= 8:
            name = self._name + ' (CR 1)'
        if level >= 11:
            name = self._name + ' (CR 2)'
        if level >= 14:
            name = self._name + ' (CR 3)'
        if level >= 17:
            name = self._name + ' (CR 4)'
        return name

    
class DivineIntervention(Feature):
    """Beginning at 10th level, you can call on your deity to intervene on your
    behalf when your need is great.

    Imploring your deity’s aid requires you to use your action. Describe the
    assistance you seek, and roll percentile dice. If you roll a number equal
    to or lower than your cleric level, your deity intervenes. The DM chooses
    the nature of the intervention; the effect of any cleric spell or cleric
    domain spell would be appropriate.

    If your deity intervenes, you can’t use this feature again for 7
    days. Otherwise, you can use it again after you finish a long rest.

    At 20th level, your call for intervention succeeds automatically, no roll
    required.

    """
    name = "Divine Intervention"
    source = "Cleric"


# Tempest Domain
class WrathOfTheStorm(Feature):
    """Also at 1st level, you can thunderously rebuke attackers. When a creature
    within 5 feet of you that you can see hits you with an attack, you can use
    your reaction to cause the creature to make a Dexterity saving throw. The
    creature takes 2d8 lightning or thunder damage (your choice) on a failed
    saving throw, and half as much damage on a successful one.

    You can use this feature a number of times equal to your Wisdom modifier (a
    minimum of once). You regain all expended uses when you finish a long rest.

    """
    _name = "Wrath of the Storm"
    source = "Cleric (Tempest Domain)"

    @property
    def name(self):
        num_uses = max(1, self.owner.wisdom.modifier)
        return self._name + ' ({:d}x/LR)'.format(num_uses)


class DestructiveWrath(ChannelDivinity):
    """Starting at 2nd level, you can use your Channel Divinity to wield the power
    of the storm with unchecked ferocity.

    When you roll lightning or thunder damage, you can use your Channel
    Divinity to deal maximum damage, instead of rolling.

    """
    name = "Channel Divinity: Destructive Wrath"
    source = "Cleric (Tempest Domain)"
    

class ThunderboltStrike(Feature):
    """At 6th level, when you deal lightning damage to a Large or smaller
    creature, you can also push it up to 10 feet away from you.

    """
    name = "Thunderbolt Strike"
    source = "Cleric (Tempest Domain)"


class DivineStrikeTempest(Feature):
    """At 8th level, you gain the ability to infuse your weapon strikes with
    divine energy. Once on each of your turns when you hit a creature with a
    weapon attack, you can cause the attack to deal an extra 1d8 thunder damage
    to the target. When you reach 14th level, the extra damage increases to
    2d8.

    """
    _name = "Divine Strike"
    source = "Cleric (Tempest Domain)"
    
    @property
    def name(self):
        level = self.owner.Cleric.level
        if level < 14:
            return self._name + " (1d8)"
        else:
            return self._name + " (2d8)"


class Stormborn(Feature):
    """At 17th level, you have a flying speed equal to your current walking speed
    whenever you are not underground or indoors. 
    """
    name = "Stormborn"
    source = "Cleric (Tempest Domain)"
