class urPoke:
    def __init__(self, name, type1, type2, health, atk, defence, spatk, spdef, spd, move1, move2):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.health = health
        self.atk = atk
        self.defence = defence
        self.spatk = spatk
        self.spdef = spdef
        self.spd = spd
        self.move1 = move1
        self.move2 = move2
    def isAlive(self):
        return self.health > 0
