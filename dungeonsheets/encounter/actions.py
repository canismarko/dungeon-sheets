from abc import ABC, abstractmethod

from dungeonsheets.encounter.events import Event


class Executable(ABC):
    """Something (like an action) that can be executed.

    Executing an action results in an event that is stored
    """

    @abstractmethod
    def execute(self, subj, obj=None):
        """Execute the given action"""


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
