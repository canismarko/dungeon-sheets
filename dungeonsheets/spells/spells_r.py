from dungeonsheets.spells.spells import Spell


class RaiseDead(Spell):
	"""You return a dead creature you touch to life, provided that it has 
	been dead no longer than 10 days. If the creature's soul is both 
	willing and at liberty to rejoin the body, the creature returns to life 
	with 1 hit point.This spell also neutralizes any poisons and cures 
	nonmagical diseases that affected the creature at the time it died. 
	This spell doesn't, however, remove magical diseases, curses, or 
	similar effects; if these aren't first removed prior to casting the 
	spell, they take effect when the creature returns to life. The spell 
	can't return an undead creature to life.This spell closes all mortal 
	wounds, but it doesn't restore missing body parts. If the creature is 
	lacking body parts or organs integral for its survival—its head, for 
	instance—the spell automatically fails.Coming back from the dead is 
	an ordeal. The target takes a −4 penalty to all attack rolls, saving 
	throws, and ability checks. Every time the target finishes a long rest, 
	the penalty is reduced by 1 until it disappears.
	
	"""

	name = "Raise Dead"
	level = 5
	casting_time = "1 Hr."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a diamond worth at least 500 gp, which the spell consumes;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Bard", "Cleric", "Paladin")
class RarysTelepathicBond(Spell):
	"""You forge a telepathic link among up to eight willing creatures of 
	your choice within range, psychically linking each creature to all the 
	others for the duration. Creatures with Intelligence scores of 2 or 
	less aren't affected by this spell.Until the spell ends, the targets 
	can communicate telepathically through the bond whether or not they 
	have a common language. The communication is possible over any 
	distance, though it can't extend to other planes of existence.
	
	"""

	name = "Rarys Telepathic Bond"
	level = 5
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("V", "S", "M")
	materials = "pieces of eggshell from two different kinds of creatures;"
	duration = "1 hour"
	ritual = True
	magic_school = "Divination"
	classes = ("Wizard","Bard")
class RaulothimsPsychicLance(Spell):
	"""You unleash a shimmering lance of psychic power from your forehead 
	at a creature that you can see within range. Alternatively, you can 
	utter a creature's name. If the named target is within range, it 
	becomes the spell's target even if you can't see it. If the named 
	target isn't within range, the lance dissipates without effect.The 
	target must make an Intelligence saving throw. On a failed save, the 
	target takes 7d6 psychic damage and is incapacitated until the start of 
	your next turn. On a successful save, the creature takes half as much 
	damage and isn't incapacitated.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, the damage increases by 1d6 for each slot level 
	above 4th."""

	name = "Raulothims Psychic Lance"
	level = 4
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
class RaulothimsPsychicLance(Spell):
	"""You unleash a shimmering lance of psychic power from your forehead 
	at a creature that you can see within range. Alternatively, you can 
	utter the creature's name. If the named target is within range, it 
	gains no benefit from cover or invisibility as the lance homes in on 
	it. If the named target isn't within range, the lance dissipates, and 
	the spell slot is not expended.The target must succeed on an 
	Intelligence saving throw or take 10d6 psychic damage and be 
	incapacitated until the start of your next turn.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, the damage increases by 1d6 for each slot level 
	above 4th."""

	name = "Raulothims Psychic Lance"
	level = 4
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
class RavenousVoid(Spell):
	"""You create a 20-foot-radius sphere of destructive gravitational 
	force centered on a point you can see within range. For the spell's 
	duration, the sphere and any space within 100 feet of it are difficult 
	terrain, and nonmagical objects fully inside the sphere are destroyed 
	if they aren't being worn or carried.When the sphere appears and at the 
	start of each of your turns until the spell ends, unsecured objects 
	within 100 feet of the sphere are pulled toward the sphere's center, 
	ending in an unoccupied space as close to the center as possible.A 
	creature that starts its turn within 100 feet of the sphere must 
	succeed on a Strength saving throw or be pulled straight toward the 
	sphere's center, ending in an unoccupied space as close to the center 
	as possible. A creature that enters the sphere for the first time on a 
	turn or starts its turn there takes 5d10 force damage and is restrained 
	until it is no longer in the sphere. If the sphere is in the air, the 
	restrained creature hovers inside the sphere. A creature can use its 
	action to make a Strength check against your spell save DC, ending this 
	restrained condition on itself or another creature in the sphere that 
	it can reach. A creature reduced to 0 hit points by this spell is 
	annihilated, along with any nonmagical items it is wearing or carrying.
	
	"""

	name = "Ravenous Void"
	level = 9
	casting_time = "Action"
	casting_range = "1000 feet"
	components = ("V", "S", "M")
	materials = "a small, nine-pointed star made of iron;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Evocation"
	classes = ()
class RayOfEnfeeblement(Spell):
	"""A black beam of enervating energy springs from your finger toward a 
	creature within range. Make a ranged spell attack against the target. 
	On a hit, the target deals only half damage with weapon attacks that 
	use Strength until the spell ends.At the end of each of the target's 
	turns, it can make a Constitution saving throw against the spell. On a 
	success, the spell ends.
	
	"""

	name = "Ray of Enfeeblement"
	level = 2
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Warlock", "Wizard")
class RayOfFrost(Spell):
	"""A frigid beam of blue-white light streaks toward a creature within 
	range. Make a ranged spell attack against the target. On a hit, it 
	takes 1d8 cold damage, and its speed is reduced by 10 feet until the 
	start of your next turn.The spell's damage increases by 1d8 when you 
	reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).
	
	"""

	name = "Ray of Frost"
	level = 0
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Artificer", "Sorcerer", "Wizard")
class RayOfSickness(Spell):
	"""A ray of sickening greenish energy lashes out toward a creature 
	within range. Make a ranged spell attack against the target. On a hit, 
	the target takes 2d8 poison damage and must make a Constitution saving 
	throw. On a failed save, it is also poisoned until the end of your next 
	turn.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	2nd level or higher, the damage increases by 1d8 for each slot level 
	above 1st."""

	name = "Ray of Sickness"
	level = 1
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Sorcerer", "Wizard")
class RealityBreak(Spell):
	"""You shatter the barriers between realities and timelines, thrusting 
	a creature into turmoil and madness. The target must succeed on a 
	Wisdom saving throw, or it can't take reactions until the spell ends. 
	The affected target must also roll a d10 at the start of each of its 
	turns; the number rolled determines what happens to the target, as 
	shown on the Reality Break Effects table.At the end of each of its 
	turns, the affected target can repeat the Wisdom saving throw, ending 
	the spell on itself on a success.Reality Break 
	Effectsd10Effect1-2Vision of the Far Realm. The target takes 6d12 
	psychic damage, and it is stunned until the end of the turn.3-5Rending 
	Rift. The target must make a Dexterity saving throw, taking 8d12 force 
	damage on a failed save, or half as much damage on a successful 
	one.6-8Wormhole. The target is teleported, along with everything it is 
	wearing and carrying, up to 30 feet to an unoccupied space of your 
	choice that you can see. The target also takes 10d12 force damage and 
	is knocked prone.9-10Chill of the Dark Void. The target takes 10d12 
	cold damage, and it is blinded until the end of the turn.
	
	"""

	name = "Reality Break"
	level = 8
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a crystal prism;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Conjuration"
	classes = ()
class Regenerate(Spell):
	"""You touch a creature and stimulate its natural healing ability. The 
	target regains 4d8 + 15 hit points. For the duration of the spell, the 
	target regains 1 hit point at the start of each of its turns (10 hit 
	points each minute).The target's severed body members (fingers, legs, 
	tails, and so on), if any, are restored after 2 minutes. If you have 
	the severed part and hold it to the stump, the spell instantaneously 
	causes the limb to knit to the stump.
	
	"""

	name = "Regenerate"
	level = 7
	casting_time = "1 Min."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a prayer wheel and holy water;"
	duration = "1 hour"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Bard", "Cleric", "Druid")
class Reincarnate(Spell):
	"""You touch a dead humanoid or a piece of a dead humanoid. Provided 
	that the creature has been dead no longer than 10 days, the spell forms 
	a new adult body for it and then calls the soul to enter that body. If 
	the target's soul isn't free or willing to do so, the spell fails.The 
	magic fashions a new body for the creature to inhabit, which likely 
	causes the creature's race to change. The DM rolls a d100 and consults 
	the following table to determine what form the creature takes when 
	restored to life, or the DM chooses a form.Reincarnate 
	Racesd100Race01-04Dragonborn05-13Dwarf, hill14-21Dwarf, 
	mountain22-25Elf, dark26-34Elf, high35-42Elf, wood43-46Gnome, 
	forest47-52Gnome, rock53-56Half-elf57-60Half-orc61-68Halfling, 
	lightfoot69-76Halfling, stout77-96Human97-00TieflingThe reincarnated 
	creature recalls its former life and experiences. It retains the 
	capabilities it had in its original form, except it exchanges its 
	original race for the new one and changes its racial traits accordingly.
	
	"""

	name = "Reincarnate"
	level = 5
	casting_time = "1 Hr."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "rare oils and unguents worth at least 1,000 gp, which the spell consumes;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Druid")
class RemoteAccess(Spell):
	"""You can use any electronic device within range as if it were in your 
	hands. This is not a telekinesis effect. Rather, this spell allows you 
	to simulate a device's mechanical functions electronically. You are 
	able to access only functions that a person using the device manually 
	would be able to access. You can use remote access with only one device 
	at a time.
	
	"""

	name = "Remote Access"
	level = 1
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "10 minutes"
	ritual = False
	magic_school = "Transmutation (technomagic)"
	classes = ("Sorcerer", "Warlock", "Wizard")
class RemoveCurse(Spell):
	"""At your touch, all curses affecting one creature or object end. If 
	the object is a cursed magic item, its curse remains, but the spell 
	breaks its owner's attunement to the object so it can be removed or 
	discarded.
	
	"""

	name = "Remove Curse"
	level = 3
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Cleric", "Paladin", "Warlock", "Wizard")
class Resistance(Spell):
	"""You touch one willing creature. Once before the spell ends, the 
	target can roll a d4 and add the number rolled to one saving throw of 
	its choice. It can roll the die before or after making the saving 
	throw. The spell then ends.
	
	"""

	name = "Resistance"
	level = 0
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a miniature cloak;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Artificer", "Cleric", "Druid")
class Resurrection(Spell):
	"""You touch a dead creature that has been dead for no more than a 
	century, that didn't die of old age, and that isn't undead. If its soul 
	is free and willing, the target returns to life with all its hit 
	points.This spell neutralizes any poisons and cures normal diseases 
	afflicting the creature when it died. It doesn't, however, remove 
	magical diseases, curses, and the like; if such effects aren't removed 
	prior to casting the spell, they afflict the target on its return to 
	life.This spell closes all mortal wounds and restores any missing body 
	parts.Coming back from the dead is an ordeal. The target takes a −4 
	penalty to all attack rolls, saving throws, and ability checks. Every 
	time the target finishes a long rest, the penalty is reduced by 1 until 
	it disappears.Casting this spell to restore life to a creature that has 
	been dead for one year or longer taxes you greatly. Until you finish a 
	long rest, you can't cast spells again, and you have disadvantage on 
	all attack rolls, ability checks, and saving throws.
	
	"""

	name = "Resurrection"
	level = 7
	casting_time = "1 Hr."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a diamond worth at least 1,000 gp, which the spell consumes;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Bard", "Cleric")
class ReverseGravity(Spell):
	"""This spell reverses gravity in a 50-foot-radius, 100-foot-high 
	cylinder centered on a point within range. All creatures and objects 
	that aren't somehow anchored to the ground in the area fall upward and 
	reach the top of the area when you cast this spell. A creature can make 
	a Dexterity saving throw to grab onto a fixed object it can reach, thus 
	avoiding the fall.If some solid object (such as a ceiling) is 
	encountered in this fall, falling objects and creatures strike it just 
	as they would during a normal downward fall. If an object or creature 
	reaches the top of the area without striking anything, it remains 
	there, oscillating slightly, for the duration.At the end of the 
	duration, affected objects and creatures fall back down.
	
	"""

	name = "Reverse Gravity"
	level = 7
	casting_time = "Action"
	casting_range = "100 feet"
	components = ("V", "S", "M")
	materials = "a lodestone and iron filings;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Druid", "Sorcerer", "Wizard")
class Revivify(Spell):
	"""You touch a creature that has died within the last minute. That 
	creature returns to life with 1 hit point. This spell can't return to 
	life a creature that has died of old age, nor can it restore any 
	missing body parts.
	
	"""

	name = "Revivify"
	level = 3
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "diamonds worth 300 gp, which the spell consumes;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Artificer", "Cleric", "Paladin","Druid", "Ranger")
class RimesBindingIce(Spell):
	"""A burst of cold energy emanates from you in a 30-foot cone. Each 
	creature in that area must make a Constitution saving throw. On a 
	failed save, a creature takes 3d8 cold damage and is hindered by ice 
	formations for 1 minute, or until it or another creature within reach 
	of it uses an action to break away the ice. A creature hindered by ice 
	has its speed reduced to 0. On a successful save, a creature takes half 
	as much damage and isn't hindered by ice.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, increase the cold damage by 1d8 for each slot 
	level above 2nd."""

	name = "Rimes Binding Ice"
	level = 2
	casting_time = "Action"
	casting_range = "Self (30-foot cone)"
	components = ("S", "M")
	materials = "a vial of meltwater;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Sorcerer", "Wizard")
class RopeTrick(Spell):
	"""You touch a length of rope that is up to 60 feet long. One end of 
	the rope then rises into the air until the whole rope hangs 
	perpendicular to the ground. At the upper end of the rope, an invisible 
	entrance opens to an extradimensional space that lasts until the spell 
	ends.The extradimensional space can be reached by climbing to the top 
	of the rope. The space can hold as many as eight Medium or smaller 
	creatures. The rope can be pulled into the space, making the rope 
	disappear from view outside the space.Attacks and spells can't cross 
	through the entrance into or out of the extradimensional space, but 
	those inside can see out of it as if through a 3-foot-by-5-foot window 
	centered on the rope.Anything inside the extradimensional space drops 
	out when the spell ends.
	
	"""

	name = "Rope Trick"
	level = 2
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "powdered corn extract and a twisted loop of parchment;"
	duration = "1 hour"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Wizard")
