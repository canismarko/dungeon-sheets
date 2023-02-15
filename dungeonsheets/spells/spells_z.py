from dungeonsheets.spells.spells import Spell


class ZephyrStrike(Spell):
	"""You move like the wind. Until the spell ends, your movement doesn't 
	provoke opportunity attacks.Once before the spell ends, you can give 
	yourself advantage on one weapon attack roll on your turn. That attack 
	deals an extra 1d8 force damage on a hit. Whether you hit or miss, your 
	walking speed increases by 30 feet until the end of that turn.
	
	"""

	name = "Zephyr Strike"
	level = "1"
	casting_time = "Bonus"
	casting_range = "Self"
	components = "V"
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Ranger")
class ZephyrStrike(UA)(Spell):
	"""You move like the wind. For the duration, your movement doesn't 
	provoke opportunity attacks.In addition, the first time you make a 
	weapon attack on your turn before the spell ends, you make the attack 
	roll with advantage, and your speed increases by 30 feet until the end 
	of that turn.
	
	"""

	name = "Zephyr Strike (UA)"
	level = "1"
	casting_time = "Bonus"
	casting_range = "Self"
	components = "V"
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Ranger")
