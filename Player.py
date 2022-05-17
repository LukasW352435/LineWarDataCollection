class Player:
    rank = 0
    name = ""
    skill = 0
    skill_true = 0
    wins = 0
    loses = 0
    extra = ""
    skill_increase = 0
    wins_in_a_row = 0

    def __init__(self):
        pass

    def __str__(self):
        self.split_extra()
        return str(self.rank) + "; " + self.name + "; " + str(self.skill_true).replace(".", ",") + "; " + str(self.wins) + "; " + str(self.loses) + "; " + str(self.wins_in_a_row) + "; " + str(self.skill_increase).replace(".", ",") + "; "

    def split_extra(self):
        if len(self.extra) < 1:
            return
        sp = self.extra.split(" ")
        if len(sp) < 15:
            raise ValueError(self.extra)
        sp.reverse()
        self.skill_increase = float(sp[2])
        self.wins_in_a_row = int(sp[12])