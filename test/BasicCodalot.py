from test.Codalot import Codalot
from test.KnightPosition import KnightPosition


class BasicCodalot(Codalot):

    knights = []

    def __init__(self):
        self.knights = list()
        for i in range(6):
            self.knights.append(Knight())

    def setKnight(self, index, position):
        knight = self.knights[index]
        knight.setInTavern(False)
        knight.setInTrainingYard(False)
        if position == KnightPosition.TAVERN:
            knight.setInTavern(True)
        elif position == KnightPosition.TRAINING_YARD:
            knight.setInTrainingYard(True)

    def process(self):
        for knight in self.knights:
            knight.incrementStamina(1 if knight.isInTavern() else -1)
            knight.incrementXp(1 if knight.isInTrainingYard() else 0)

    def calculateEarnedXp(self):
        total = 0
        for knight in self.knights:
            total += knight.getXp()
        return total

    def clearKnights(self):
        self.knights.clear()

    def addKnightToTrainingYard(self, knight):
        self.knights.append(knight)
        knight.set_in_training_yard(True)
        knight.set_in_tavern(False)

    def addKnightToTavern(self, knight):
        self.knights.append(knight)
        knight.set_in_tavern(True)
        knight.set_in_training_yard(False)

    def grantBonusXp(self):
        bonusKnights = 0
        for knight in self.knights():
            if knight.getXp() >= 3:
                bonusKnights = bonusKnights + 1

        if bonusKnights == 3:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 5)

        if bonusKnights == 5:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 10)

        if bonusKnights == 6:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 20)


class Knight(object):
    __isInTavern = False
    __isInTrainingYard = False

    def __init__(self):
        self.__xp = 0
        self.__stamina = 0

    def getXp(self):
        return self.__xp

    def setXp(self, xp):
        self.__xp = xp

    def incrementXp(self, xp):
        self.__xp += xp

    def getStamina(self):
        return self.__stamina

    def setStamina(self, stamina):
        self.__stamina = stamina

    def incrementStamina(self, stamina):
        self.__stamina = self.__stamina + 1

    def isInTavern(self):
        return self.__isInTavern

    def setInTavern(self, isInTavern):
        self.__isInTavern = isInTavern

    def isInTrainingYard(self):
        return self.__isInTrainingYard

    def setInTrainingYard(self, isInTrainingYard):
        self.__isInTrainingYard = isInTrainingYard
