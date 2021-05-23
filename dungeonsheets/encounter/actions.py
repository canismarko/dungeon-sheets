from abc import ABC, abstractmethod

class Event:
    """An event between one and possibly more entities"""

    subj = None
    obj = None

    def __init__(self, action, subj, obj):
        self.action = action
        self.subj = subj
        self.obj = obj


class Executable(ABC):
    """Something (like an action) that can be executed.

    Executing an action results in an event that is stored
    """

    @abstractmethod
    def execute(self, subj, obj=None):
        return Event(self, subj, obj)


class Action(Executable):
    pass


class BonusAction(Executable):
    pass


class Reaction(Executable):
    pass


class Movement(Executable):
    pass


class LairAction(Executable):
    pass


class LegendaryAction(Executable):
    pass


class Attack(Action):

    def __init__(self, subj, obj):
        self.subj = subj
        self.obj = obj

    def execute(self):
        # Subject makes an attack roll
        # Compare attack roll to object's AC
        # Store the results to look into the event later

        pass  # TODO: Write how to do this
