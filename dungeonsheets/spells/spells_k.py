from dungeonsheets.spells.spells import Spell


class KineticJaunt(Spell):
	"""You magically empower your movement with dance-like steps, giving 
	yourself the following benefits for the duration.Your walking speed 
	increases by 10 feet.You don't provoke opportunity attacks.You can move 
	through the space of another creature, and it doesn't count as 
	difficult terrain. If you end your turn in another creature's space, 
	you are shunted to the last unoccupied space you occupied, and you take 
	1d8 force damage.
	
	"""

	name = "Kinetic Jaunt"
	level = 2
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Bard", "Sorcerer", "Wizard")
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
	level = 2
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Bard", "Sorcerer", "Wizard")
