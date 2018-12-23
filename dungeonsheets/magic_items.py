class MagicItem():
    """
    Generic Magic Item. Add description here.

    """
    name = ''
    ac_bonus = 0
    requires_attunement = False
    rarity = ''


class RingOfProtection(MagicItem):
    """
    You gain a +1 bonus to AC and Saving Throws while wearing this ring.

    """
    name = "Ring of Protection"
    ac_bonus = 1
    requires_attunement = True
    rarity = 'Rare'
