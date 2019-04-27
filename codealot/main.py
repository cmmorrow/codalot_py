from random import Random


class Knight(object):

    __is_in_tavern = False
    __is_in_training_yard = False

    def __init__(self):
        self.xp = 0
        self.stamina = 0

    def increment_xp(self, xp):
        self.xp += xp

    def increment_stamina(self, stamina):
        self.stamina += stamina

    def is_in_tavern(self):
        return self.__is_in_tavern

    def set_in_tavern(self, status):
        self.__is_in_tavern = status

    def is_in_training_yard(self):
        return self.__is_in_training_yard

    def set_in_training_yard(self, status):
        self.__is_in_training_yard = status


class Codalot(object):

    knights = []

    def __init__(self):
        self.knights = []

    def clear_knights(self):
        del self.knights[:]

    def add_knight_to_training_yard(self, knight):
        self.knights.append(knight)
        knight.set_in_training_yard(True)
        knight.set_in_tavern(False)

    def add_knight_to_tavern(self, knight):
        self.knights.append(knight)
        knight.set_in_tavern(True)
        knight.set_in_training_yard(False)

    def process(self):
        for knight in self.knights:
            knight.increment_stamina(1 if knight.is_in_tavern() else -1)
            knight.increment_xp(1 if knight.is_in_training_yard() else 0)

    def grant_bonus_xp(self):
        bonus_knights = 0
        for knight in self.knights:
            if knight.xp >= 3:
                bonus_knights = bonus_knights + 1

        if bonus_knights == 3:
            for knight in self.knights:
                if knight.xp >= 3:
                    knight.xp += 5

        if bonus_knights == 5:
            for knight in self.knights:
                if knight.xp >= 3:
                    knight.xp += 10

        if bonus_knights == 6:
            for knight in self.knights:
                if knight.xp >= 3:
                    knight.xp += 20


if __name__ == "__main__":
    codalot = Codalot()

    knights = []
    for i in range(6):
        knights.append(Knight())

    random = Random(1)
    for _ in range(24):
        codalot.clear_knights()
        for knight in knights:
            random_val = random.randint(0, 1)
            if random_val == 0:
                codalot.add_knight_to_training_yard(knight)
            elif random_val == 1:
                codalot.add_knight_to_tavern(knight)
        codalot.process()
    codalot.grant_bonus_xp()

    total_xp = 0
    for knight in knights:
        total_xp += knight.xp

print("Total XP earned by all " + str(len(knights)) + " knights: " + str(total_xp))
