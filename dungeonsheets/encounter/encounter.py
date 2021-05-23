class Encounter:
    """A combat encounter between two parties -- good guys and bad guys"""

    def __init__(self, group_a, group_b):
        self.group_a = group_a
        self.group_b = group_b
        self.all_agents = group_a + group_b

        self.events = []  # Should be private?

    def opponents(self, agent):
        """Who opposes the given agent in an encounter?"""
        if agent in self.group_a:
            return self.group_b
        else:
            return self.group_a

    def allies(self, agent):
        """Who sides with the given agent in an encounter?"""
        if agent in self.group_a:
            return list(set(self.group_a) - set([agent]))
        else:
            return list(set(self.group_b) - set([agent]))

    def reset(self):
        self.events = []
        self.long_rest()

    def simulate(self):
        """Who will win?"""

        # Initiative
        for agent in self.all_agents:
            agent.roll_initiative()

        self.all_agents = sorted(self.all_agents, key=lambda a: a.initiative_roll)

        # TODO: Support Lair Actions, cleverer loop
        while not self.is_encounter_over():
            self.new_turn()
            for agent in self.all_agents:
                agent.make_actions(self)
                if self.is_encounter_over():
                    return self.events

        return self.events  # Should never get here -- self.is_encounter_over() will end it

    def rating(self):
        """Encounter Rating"""
        raise NotImplementedError()

    def is_encounter_over(self):
        """If all members of one party are at HP <= 0, it's over"""
        return (
                all([agent.current_hp <= 0 for agent in self.group_a]) or
                all([agent.current_hp <= 0 for agent in self.group_b])
        )

    def long_rest(self):
        """Resets all agents to have full actions, abilities, etc."""
        for agent in self.all_agents:
            agent.long_rest()

    def new_turn(self):
        """Resets turn-based actions for all agents"""
        for agent in self.all_agents:
            agent.new_turn()

