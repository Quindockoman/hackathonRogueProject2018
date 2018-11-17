# Monster Class

class monster:
    # combat-related properties and methods (monster, player, NPC).
    def __init__(self, speed, strength, knowledge, sanity, death_function=None):
        self.base_speed = speed
        self.base_strength = strength
        self.base_knowledge = knowledge
        self.base_sanity = sanity
        self.death_function = death_function


    @property
    def strength(self):  # return actual strength, by summing up the bonuses from all equipped items
        return self.base_strength

    @property
    def speed(self):  # return actual speed, by summing up the bonuses from all equipped items
        return self.base_speed

    @property
    def knowledge(self):  # return actual knowledge, by summing up the bonuses from all equipped items
        return self.base_knowledge

    @property
    def sanity(self):  # return actual sanity, by summing up the bonuses from all equipped items
        return self.base_sanity

