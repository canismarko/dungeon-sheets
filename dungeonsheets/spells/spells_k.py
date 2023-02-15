from dungeonsheets.spells.spells import Spell


class Knock(Spell):
	"""Choose an object that you can see within range. The object can be a 
	door, a box, a chest, a set of manacles, a padlock, or another object 
	that contains a mundane or magical means that prevents access.A target 
	that is held shut by a mundane lock or that is stuck or barred becomes 
	unlocked, unstuck, or unbarred. If the object has multiple locks, only 
	one of them is unlocked.If you choose a target that is held shut with 
	arcane lock, that spell is suppressed for 10 minutes, during which time 
	the target can be opened and shut normally.When you cast the spell, a 
	loud knock, audible from as far away as 300 feet, emanates from the 
	target object.
	
	"""

	name = "Knock"
	level = "2"
	casting_time = "Action"
	casting_range = "60 feet"
	components = "V"
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Bard", "Sorcerer", "Wizard")
