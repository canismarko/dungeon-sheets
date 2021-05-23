class Encounter:
    """A combat encounter between two parties -- good guys and bad guys"""

    def __init__(self, *parties):
        if len(parties) < 2:
            raise ValueError("You need at least 2 parties to hold an encounter")
        if len(parties) is not 2:
            raise NotImplementedError("Haven't implemented AI for 3+ groups")  # TODO: Implement this

        # Combine all parties into a single group
        self.all_agents = parties[0]
        for party in parties[1:]:
            self.all_agents += party

    def rating(self):
        raise NotImplementedError()  # Deadly for Python :/

    def simulate(self):
        """Who will win?"""

        # Initiative
        for agent in self.all_agents:
            agent.roll_initiative()
        self.all_agents = sorted(self.all_agents, key=lambda a: a.initiative_roll)

        raise NotImplementedError()  # Apparently the mind flayers win for now

    def analyze(self):
        """So, really... how deadly *is* it?"""
        raise NotImplementedError()  # TODO: Run a Monte-Carlo simulation
