class Agent:
    """An actor in an encounter"""

    strategies = ("Random", "Greedy", "KillWeakest")
    strategy = "Greedy"

    def __init__(self):
        pass

    @property
    def actions(self):
        """All the things I can do in a turn"""
        raise NotImplementedError()
    
    @property
    def free_actions(self):
        """Stuff I can do as much as I want in a turn"""
        raise NotImplementedError()

    @property
    def movement(self):
        """Where I can go in a turn"""
        raise NotImplementedError()

    @property
    def bonus_actions(self):
        """Things I can do once in addition to an action"""
        raise NotImplementedError()

    @property
    def reactions(self):
        """Things I can do in response to an action"""
        raise NotImplementedError()

    @property
    def lair_actions(self):
        """Things I can do at initiative count 20"""
        raise NotImplementedError()

    @property
    def legendary_actions(self):
        """Things I can do so many times in a turn after another agent acts"""
        raise NotImplementedError()