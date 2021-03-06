# Event Class
from Player import *
from omen import *


class event:
    def __init__(self, name, description, target, power, stat, effect, room, omen):
        self.name = name
        self.description = description
        self.target = target
        self.power = power
        self.stat = stat
        self.effect = effect
        self.room = room
        self.omen = omen

    def activate(self):
        self.activate_omen()
        if self.target == "all":
            self.target_all()
        if self.target == "player":
            self.target_player()
        if self.target == "room":
            self.target_room()

    def target_all(self):
        for character in characters:
            if roll(character.get_stat(self.stat)) >= self.power:
                print(character, "Succeeds the roll")
            else:
                print(character, "Failed the roll")
                character.damage_stat(self.stat, self.effect)

    def target_player(self):
        character = self.room.get_player()
        if roll(character.get_stat(self.stat)) >= self.power:
            print(character, "Succeeds the roll")
        else:
            print(character, "Failed the roll")
            character.damage_stat(self.stat, self.effect)

    def target_room(self):
        self.room.increase_movement(self.effect)

    def activate_omen(self):
        if self.omen:
            omen.set_count()

