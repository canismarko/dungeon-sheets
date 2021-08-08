from dungeonsheets.content_registry import default_content_registry


default_content_registry.add_module(__name__)


class MagicItem:
    """
    Generic Magic Item. Add description here.

    """

    name = ""
    ac_bonus = 0
    st_bonus = 0
    requires_attunement = False
    needs_implementation = False
    rarity = ""
    item_type = ""

    def __init__(self, owner=None):
        self.owner = owner

    def __str__(self):
        return self.name

    def __repr__(self):
        return '"{:s}"'.format(str(self))


class CloakOfProtection(MagicItem):
    """You gain a +1 bonus to AC and Saving Throws while wearing this
    cloak.
    
    """
    name = "Cloak of Protection"
    ac_bonus = 1
    st_bonus = 1
    requires_attunement = True
    rarity = "Uncommon"


class RingOfProtection(MagicItem):
    """You gain a +1 bonus to AC and Saving Throws while wearing this
    ring.
    
    """
    name = "Ring of Protection"
    ac_bonus = 1
    st_bonus = 1
    requires_attunement = True
    rarity = "Rare"
    item_type = "Ring"


class DecanterOfEndlessWater(MagicItem):
    """This stoppered flask sloshes when shaken, as if it contains water. The
    decanter weighs 2 pounds.

    You can use an action to remove the stopper and speak one of three command
    words, whereupon an amount of fresh water or salt water (your choice) pours
    out of the flask. The water stops pouring out at the start of your next
    turn. Choose from the following options:

    --"Stream" produces 1 gallon of water.

    --"Fountain" produces 5 gallons of water.

    --"Geyser" produces 30 gallons of water that gushes forth in a geyser 30
    feet long and 1 foot wide. As a bonus action while holding the decanter,
    you can aim the geyser at a creature you can see within 30 feet of you. The
    target must succeed on a DC 13 Strength saving throw or take 1d4
    bludgeoning damage and fall prone. Instead of a creature, you can target an
    object that isn't being worn or carried and that weighs no more than 200
    pounds. The object is either knocked over or pushed up to 15 feet away from
    you.

    """

    name = "Decanter of Endless Water"
    rarity = "Uncommon"
    item_type = "Wondrous item"


class ToothOfAnimalFriendship(MagicItem):
    """While holding this wolf's tooth, you can expend it's one charge to cast
    Animal Friendship (DC 13) or Speak With Animals.

    The charge resets at the next Dawn.
    """

    name = "Tooth of Animal Friendship"
    rarity = "Uncommon"


class CloakOfBillowing(MagicItem):
    """While wearing this cloak, you can use a bonus action to make it billow
    dramatically.

    """

    name = "Cloak of Billowing"
    rarity = "Common"


class CloakOfDisplacement(MagicItem):
    """While you wear this cloak, it projects an illusion that makes you appear
    to be standing in a place near your actual location, causing any creature
    to have disadvantage on attack rolls against you. If you take damage, the
    property ceases to function until the start of your next turn. This
    property is suppressed while you are incapacitated, restrained, or
    otherwise unable to move.
    """

    name = "Cloak of Displacement"
    rarity = "Rare"


class CapeOfTheMountebank(MagicItem):
    """This cape smells faintly of brimstone. While wearing it, you can use it to
    cast the Dimension Door spell as an action. This property of the cape can't
    be used again until the next dawn.

    When you disappear, you leave behind a cloud of smoke, and you appear in a
    similar cloud of smoke at your destination. The smoke lightly obscures the
    space you left and the space you appear in, and it dissipates at the end of
    your next turn. A light or stronger wind disperses the smoke.

    """

    name = "Cape of the Mountebank"
    rarity = "Rare"
    requires_attunement = True


class EyesOfCharming(MagicItem):
    """These Crystal lenses fit over the eyes. They have 3 Charges. While wearing
    them, you can expend 1 charge as an action to cast the Charm Person spell
    (save DC 13) on a humanoid within 30 feet of you, provided that you and the
    target can see each other. The lenses regain all expended Charges daily at
    dawn.

    """

    name = "Eyes of Charming"
    rarity = "Uncommon"
    requires_attunement = True


class CharlattansDie(MagicItem):
    """Whenever you roll this six-sided die, you can control which number it
    rolls.

    """

    name = "Charlattan's Die"
    rarity = "Common"


class PipeOfSmokeMonsters(MagicItem):
    """While smoking this pipe, you can use an action to ex- hale a puff of smoke
    that takes the form of a single crea- ture, such as a dragon, a flumph, or
    a froghemoth. The form must be small enough to fit in a 1-foot cube and
    loses its shape after a few seconds, becoming an ordi- nary puff of smoke.

    """

    name = "Pipe of Smoke Monsters"
    rarity = "Common"


class CoinsOfCommunication(MagicItem):
    """This set of multiple coins are virtually indistinguishable from regular Gold
    Pieces, but are connected by magic. Once per day, a holder of any of any
    coin can whisper a single word into it, after which all coins will
    immediately vibrate and the word will replace a word in the traditional
    Kings Message imprinted on the coin. This ability cannot be used again by
    the holder of any of the coins until the following dawn.

    """

    name = "Coins of Communication"
    rarity = "Uncommon"


class FlameTongue(MagicItem):
    """You can use a Bonus Action to speak this magic sword's Command Word, causing
    flames to erupt from the blade. These flames shed bright light in a 40-foot
    radius and dim light for an additional 40 feet. While the sword is ablaze,
    it deals an extra 2d6 fire damage to any target it hits. The flames last
    until you use a Bonus Action to speak the Command Word again or until you
    drop or sheathe the sword

    """

    name = "Flame Tongue"
    rarity = "Rare"
    requires_attunement = True


class SpearOfLightning(MagicItem):
    """When you hurl it and speak its Command Word, it transforms into a bolt of
    lightning, forming a line 5 feet wide that extends out from you to a target
    within 120 feet. Each creature in the line excluding you and the target
    must make a DC 13 Dexterity saving throw, taking 4d6 lightning damage on a
    failed save, and half as much damage on a successful one. The Lightning
    Bolt turns back into a spear when it reaches the target.

    Make a ranged weapon Attack against the target. On a hit, the target takes
    damage from the spear plus 4d6 lightning damage.

    The spear's property can't be used again until the next dawn. In the
    meantime, the spear can still be used as a Magic Weapon.
    """

    requires_attunement = True
    name = "Lightning Spear"


class AmuletOfTheEel(MagicItem):
    """While holding this amulet, you can breath water and air, and have a
    swimming speed of 20'."""

    name = "Amulet of the Eel"


class BracersOfMagnetism(MagicItem):
    """When wearing these bracers, you can use a bonus action to speak their
    command word, causing them to become magnetically attractive to each other.

    While active, the wearer's arms are secured together, requiring a succesful DC 25
    STR (Athletics) check to separate them by six inches. The wearer has advantage
    on all STR (Athletics) checks made to grapple, but disadvantage on all
    weapon attacks and DEX (Sleight of Hand) checks.

    The wearer can use another bonus action to speak the command word and
    deactivate the magnetic effect.

    The magnetic effect fails if the bracers are more than 10' apart.
    """

    requires_attunement = True
    name = "Bracers of Magnetism"


class ShieldOfFaces(MagicItem):
    """This +1 metallic shield has a detailed face chisled into its front surface.
    As a bonus action, the wielder can use a bonus action to mentally command
    the shield to adopt a new emotional state (such as "smiling", "laughing",
    "crying", etc.)

    """

    requires_attunement = True
    name = "Shield of Faces"


class GlowingSword(MagicItem):
    """
    This strange longsword glows at odd times.
    """

    name = "Glowing Sword"


class PearlOfPower(MagicItem):
    """While this pearl is on your person, you can use an action to speak its
    Command Word and regain one expended spell slot. If the expended slot is of
    4th Level or higher, the new slot is 3rd Level. Once you have used
    the pearl, it can't be used again until the next dawn.
    """

    requires_attunement = True
    name = "Pearl of Power"
