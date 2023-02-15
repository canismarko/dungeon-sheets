from dungeonsheets.spells.spells import Spell


class VampiricTouch(Spell):
	"""The touch of your shadow-wreathed hand can siphon life force from 
	others to heal your wounds. Make a melee spell attack against a 
	creature within your reach. On a hit, the target takes 3d6 necrotic 
	damage, and you regain hit points equal to half the amount of necrotic 
	damage dealt. Until the spell ends, you can make the attack again on 
	each of your turns as an action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the damage increases by 1d6 for each slot level 
	above 3rd."""

	name = "Vampiric Touch"
	level = "3"
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Warlock", "Wizard","Sorcerer")
class ViciousMockery(Spell):
	"""You unleash a string of insults laced with subtle enchantments at a 
	creature you can see within range. If the target can hear you (though 
	it need not understand you), it must succeed on a Wisdom saving throw 
	or take 1d4 psychic damage and have disadvantage on the next attack 
	roll it makes before the end of its next turn.This spell's damage 
	increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 
	17th level (4d4).
	
	"""

	name = "Vicious Mockery"
	level = "Cantrip"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard")
class VirtueUA(Spell):
	"""You touch one creature, imbuing it with vitality. If the target has 
	at least 1 hit point, it gains a number of temporary hit points equal 
	to 1d4 + your spellcasting ability modifier. The temporary hit points 
	are lost when the spell ends.
	
	"""

	name = "Virtue (UA)"
	level = "Cantrip"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S")
	materials = ""
	duration = "1 round"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Cleric")
class VitriolicSphere(Spell):
	"""You point at a location within range, and a glowing 1-foot-diameter 
	ball of emerald acid streaks there and explodes in a 20-foot-radius 
	sphere. Each creature in that area must make a Dexterity saving throw. 
	On a failed save, a creature takes 10d4 acid damage and another 5d4 
	acid damage at the end of its next turn. On a successful save, a 
	creature takes half the initial damage and no damage at the end of its 
	next turn.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, the initial damage increases by 2d4 for each slot 
	level above 4th."""

	name = "Vitriolic Sphere"
	level = "4"
	casting_time = "Action"
	casting_range = "150 feet"
	components = ("V", "S", "M")
	materials = "a drop of giant slug bile"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Sorcerer", "Wizard")
class VortexWarp(Spell):
	"""You magically twist space around another creature you can see within 
	range. The target must succeed on a Constitution saving throw (the 
	target can choose to fail), or the target is teleported to an 
	unoccupied space of your choice that you can see within range. The 
	chosen space must be on a surface or in a liquid that can support the 
	target without the target having to squeeze.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, the range of the spell increases by 30 feet for 
	each slot level above 2nd."""

	name = "Vortex Warp"
	level = "2"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Artificer", "Sorcerer", "Wizard")
