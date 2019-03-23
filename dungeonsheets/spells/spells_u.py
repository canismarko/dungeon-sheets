from .spells import Spell


class UnseenServant(Spell):
    """This spell creates an invisible, mindless, shapeless force that performs simple 
    tasks at your command until the spell ends. The servant springs into existence 
    in an unoccupied space on the ground within range. It has AC 10, 1 hit point, 
    and a Strength of 2, and it can’t attack. If it drops to 0 hit points, the spell
     ends.
    
    Once on each of your turns as a bonus action, you can mentally command 
    the servant to move up to 15 feet and inteact with an object. The servant can 
    perform simple tasks that a human servant could do, such as fetching things, 
    cleaning, mending, folding clothes, lighting fires, serving food, and pouring 
    wine. Once you give the command, the servant performs the task to the best of 
    its ability until it completes the task, then waits for your next command.
    
    If 
    you command the servant to perform a task that would move it more than 60 feet 
    away from you, the spell ends.
    """
    name = "Unseen Servant"
    level = 1
    casting_time = "1 action"
    casting_range = "60 feet"
    components = ('V', 'S', 'M')
    materials = """A piece of string and a bit of wood"""
    duration = "1 hour"
    ritual = True
    magic_school = "Conjuration"
    classes = ('Bard', 'Warlock', 'Wizard')


