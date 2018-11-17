# Item Class


class item:
    def __init__(self, status, stat, bonus, name, description, event):
        self.status = status
        self.stat = stat
        self.bonus = bonus
        self.name = name
        self.description = description
        self.event = event

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

    def get_event(self):
        return self.event




