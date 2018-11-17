# Omen


class omen:
    def __init__(self):
        self.count = 0
        self.haunt = False

    def set_count(self):
        self.count = self.count + 1
        if roll(self.count) > 6:
            print("The Haunt starts")
