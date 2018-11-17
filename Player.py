# Character Class

class player:
    # combat-related properties and methods (monster, player, NPC).
    def __init__(self, name, speed, strength, knowledge, sanity, playerNum, death_function=None):
        self.name = name
        self.base_speed = int(speed)
        self.base_strength = int(strength)
        self.base_knowledge = int(knowledge)
        self.base_sanity = int(sanity)
        # self.death_function = death_function
        self.equipment = []
        self.equipped =[]
        self.playerNum = int(playerNum)

    def __init__(self, csvList):
        self.name = csvList[0]
        self.base_speed = csvList[1]
        self.base_strength = csvList[2]
        self.base_knowledge = csvList[3]
        self.base_sanity = csvList[4]
        # self.death_function = death_function
        self.equipment = []
        self.equipped =[]
        self.playerNum = csvList[5]

    @property
    def strength(self):  # return actual strength, by summing up the bonuses from all equipped items
        bonus = 0
        for item in self.equipped:
            if item.stat == "strength":
                bonus += item.bonus
        return self.base_strength + bonus

    @property
    def speed(self):  # return actual speed, by summing up the bonuses from all equipped items
        bonus = 0
        for item in self.equipped:
            if item.stat == "speed":
                bonus += item.bonus
        return self.base_speed + bonus

    @property
    def knowledge(self):  # return actual knowledge, by summing up the bonuses from all equipped items
        bonus = 0
        for item in self.equipped:
            if item.stat == "knowledge":
                bonus += item.bonus
        return self.base_knowledge + bonus

    @property
    def sanity(self):  # return actual sanity, by summing up the bonuses from all equipped items
        bonus = 0
        for item in self.equipped:
            if item.stat == "sanity":
                bonus += item.bonus
        return self.base_sanity + bonus

    def dumpStats(self):
        print(self.name)
        print(self.base_speed)
        print(self.base_strength)
        print(self.base_knowledge)
        print(self.base_sanity)
        print(self.equipment)
        print(self.equipped)

    def attack(self, target):
        # a simple formula for attack damage
        damage = self.strength - target.fighter.defense

        if damage > 0:
            # make the target take some damage
            message(self.owner.name.capitalize() + ' attacks ' + target.name + ' for ' + str(damage) + ' hit points.')
            target.fighter.take_damage(damage)
        else:
            message(self.owner.name.capitalize() + ' attacks ' + target.name + ' but it has no effect!')

    def pickup(self, item): # Takes items and adds it to the equipment list
        self.equipment.append(item)
        if(item.status == "passive"):
            self.equipped.append(item)

    def equip(self): # Should return a list of active items, that currently affect stats
        return self.equipped

    def use_item(self):
        count = 0
        option = []
        for item in self.equipment:
            if item.status == "active":
                print(count, ". ", item.name, '/n')
                option.append(item)
                self.equipped.remove(item)
                count += 1
        x = input("Please enter the number of item to activate: ")
        self.equipped.append(option[x])
        option.remove(option[x])
        for item in option:
            self.equipment.append(item)

    def destroy(self):
        for item in self.equipped:
            if(item.status == "active"):
                self.equipped.remove(item)

    def get_stat(self, stat):
        if stat == "strength":
            return self.strength()
        if stat == "speed":
            return self.speed()
        if stat == "knowledge":
            return self.knowledge()
        if stat == "sanity":
            return self.sanity()

    def damage_stat(self, stat, power):
        if stat == "strength":
            self.base_strength = self.base_strength - power
        if stat == "speed":
            self.base_speed = self.base_speed - power
        if stat == "knowledge":
            self.base_knowledge = self.base_knowledge - power
        if stat == "sanity":
            self.base_sanity = self.base_sanity - power
