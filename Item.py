# Item Class


class item:
    def __init__(self, status, stat, bonus, name, description):
        self.status = status
        self.stat = stat
        self.bonus = bonus
        self.name = name
        self.description = description

    def __init__(self, csvList):
        self.status = csvList[0]
        self.stat = csvList[1]
        self.bonus = csvList[2]
        self.name = csvList[3]
        self.description = csvList[4]

    def get_status(self):
        return self.status

    def get_stat(self):
        return self.stat

    def get_bonus(self):
        return self.bonus

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
