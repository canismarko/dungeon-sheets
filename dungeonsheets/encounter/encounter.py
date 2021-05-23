from .strategy import Strategy

class Encounter:
    """A combat encounter between two parties -- good guys and bad guys"""

    def __init__(self, good_guys, bad_guys):
        self.good_guys = good_guys
        self.bad_guys = bad_guys

    def rating(self):
        raise NotImplementedError()  # Deadly for Python :/

    def simulate(self):
        """Who will win?"""
        raise NotImplementedError()  # Apparently the mind flayers win for now

    def analyze(self):
        """So, really... how deadly *is* it?"""
        raise NotImplementedError()  # TODO: Run a Monte-Carlo simulation
