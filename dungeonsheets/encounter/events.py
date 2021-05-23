class Event:
    """An event between one and possibly more entities"""

    def __init__(self, action, *args, **kwargs):
        self.action = action
        self.subj_hp = action.subj.current_hp



class AttackEvent(Event):
    """An attack action completed"""

    def __init__(self, action, result, damage, is_hit):
        super(AttackEvent, self).__init__(action)
        if hasattr(self.action, "obj"):
            self.obj_hp = self.action.obj.current_hp
        self.result = result
        self.damage = damage
        self.is_hit = is_hit

    def __str__(self):

        if self.is_hit:
            return f"{self.action.subj.name} Hit! with a {self.result} for {self.damage} damage, leaving {self.action.obj.name} with {self.obj_hp} hitpoints"
        else:
            return f"{self.action.subj.name} Missed! with a {self.result}. {self.action.obj.name} has {self.obj_hp} hp remaining."

# TODO: Support more events
