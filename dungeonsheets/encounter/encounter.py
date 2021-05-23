class Encounter:
    """A combat encounter between two parties -- good guys and bad guys"""

    def __init__(self, group_a, group_b):
        self.group_a = group_a
        self.group_b = group_b
        self.all_agents = group_a + group_b

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
