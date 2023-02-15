from dungeonsheets.spells.spells import Spell


class NathairsMischief(Spell):
	"""You fill a 20-foot cube you can see within range with fey and 
	draconic magic. Roll on the Mischievous Surge table to determine the 
	magical effect produced, and roll again at the start of each of your 
	turns until the spell ends. You can move the cube up to 10 feet before 
	you roll.Mischievous Surged4Effect1The smell of apple pie fills the 
	air, and each creature in the cube must succeed on a Wisdom saving 
	throw or become charmed by you until the start of your next 
	turn.2Bouquets of flowers appear all around, and each creature in the 
	cube must succeed on a Dexterity saving throw or be blinded until the 
	start of your next turn as the flowers spray water in their faces.3Each 
	creature in the cube must succeed on a Wisdom saving throw or begin 
	giggling until the start of your next turn. A giggling creature is 
	incapacitated and uses all its movement to move in a random 
	direction.4Drops of molasses hover in the cube, making it difficult 
	terrain until the start of your next turn.
	
	"""

	name = "Nathairs Mischief"
	level = "2"
	casting_time = "Action"
	casting_range = "60 feet"
	components = "S, M"
	materials = "a piece of crust from an apple pie"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Illusion"
	classes = ("Bard", "Sorcerer", "Wizard")
class NegativeEnergyFlood(Spell):
	"""You send ribbons of negative energy at one creature you can see 
	within range. Unless the target is undead, it must make a Constitution 
	saving throw, taking 5d12 necrotic damage on a failed save, or half as 
	much damage on a successful one. A target killed by this damage rises 
	up as a zombie at the start of your next turn. The zombie pursues 
	whatever creature it can see that is closest to it. Statistics for the 
	zombie are in the Monster Manual.If you target an undead with this 
	spell, the target doesn't make a saving throw. Instead, roll 5d12. The 
	target gains half the total as temporary hit points.
	
	"""

	name = "Negative Energy Flood"
	level = "5"
	casting_time = "Action"
	casting_range = "60 feet"
	components = "V, M"
	materials = "a broken bone and a square of black silk"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Warlock", "Wizard")
class Nondetection(Spell):
	"""For the duration, you hide a target that you touch from divination 
	magic. The target can be a willing creature or a place or an object no 
	larger than 10 feet in any dimension. The target can't be targeted by 
	any divination magic or perceived through magical scrying sensors.
	
	"""

	name = "Nondetection"
	level = "3"
	casting_time = "Action"
	casting_range = "Touch"
	components = "V, S, M"
	materials = "a pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes"
	duration = "8 hours"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Bard", "Ranger", "Wizard")
class NystulsMagicAura(Spell):
	"""You place an illusion on a creature or an object you touch so that 
	divination spells reveal false information about it. The target can be 
	a willing creature or an object that isn't being carried or worn by 
	another creature.When you cast the spell, choose one or both of the 
	following effects. The effect lasts for the duration. If you cast this 
	spell on the same creature or object every day for 30 days, placing the 
	same effect on it each time, the illusion lasts until it is dispelled. 
	False Aura. You change the way the target appears to spells and magical 
	effects, such as detect magic, that detect magical auras. You can make 
	a nonmagical object appear magical, a magical object appear nonmagical, 
	or change the object's magical aura so that it appears to belong to a 
	specific school of magic that you choose. When you use this effect on 
	an object, you can make the false magic apparent to any creature that 
	handles the item. Mask. You change the way the target appears to spells 
	and magical effects that detect creature types, such as a paladin's 
	Divine Sense or the trigger of a symbol spell. You choose a creature 
	type and other spells and magical effects treat the target as if it 
	were a creature of that type or of that alignment.
	
	"""

	name = "Nystuls Magic Aura"
	level = "2"
	casting_time = "Action"
	casting_range = "Touch"
	components = "V, S, M"
	materials = "a small square of silk"
	duration = "24 hours"
	ritual = False
	magic_school = "Illusion"
	classes = ("Wizard")
