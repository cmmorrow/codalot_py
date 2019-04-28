"""This module hosts the main event loop and the production Knight and Codalot classes."""

from random import Random


class Knight(object):
    """This class represents a Codalot Knight."""

    __is_in_tavern = False
    __is_in_training_yard = False
    __is_at_round_table = False

    def __init__(self):
        """Initialize a new Knight object with 0 xp and stamina."""
        self.xp = 0
        self.stamina = 0
        self.round_table_counter = 0

    def increment_xp(self, xp):
        """Increase the Knight's xp by the given value.

        :param int xp: The value to increment by.
        """
        self.xp += xp

    def increment_stamina(self, stamina):
        """Increase the Knight's stamina by the given value.

        :param int stamina: The value to increment by.
        """
        self.stamina += stamina

    @property
    def is_in_tavern(self):
        """Identifies if the Knight is in the tavern or not.

        :return: True if the Knight is in the tavern else False.
        """
        return self.__is_in_tavern

    def set_in_tavern(self, status):
        """Moves the Knight in or out of the tavern.

        :param bool status: Controls the movement of the Knight in or out of the tavern.
        """
        self.__is_in_tavern = status

    @property
    def is_in_training_yard(self):
        """Identifies if the Knight is in the training yard or not.

        :return: True if the Knight is in the training yard else False.
        """
        return self.__is_in_training_yard

    def set_in_training_yard(self, status):
        """Moves the Knight in or out of the training yard.

        :param bool status: Controls the movement of the Knight in or out of the tavern.
        """
        self.__is_in_training_yard = status

    @property
    def is_at_round_table(self):
        """Identifies if the Knight is at the round table or not.

        :return True if the Knight is at the round table else False.
        """
        return self.__is_at_round_table

    def set_at_round_table(self, status):
        """Moves the Knight to or from the round table.

        :param bool status: Controls the movement of the Knight to and from the round table.
        """
        self.__is_at_round_table = status


class KingArthur(Knight):
    """King Arthur himself."""


class Codalot(object):
    """This class implements the control logic for the Knights."""

    num_of_knights = 12
    days_to_run = 1

    def __init__(self):
        """Initialize the empty list of knights."""
        self.knights = []

    def clear_knights(self):
        """Reset the list of knights."""
        self.knights = []

    def add_knight_to_training_yard(self, knight):
        """Move a specified Knight object to the training yard.

        :param Knight knight: The Knight object to move to the training yard.
        """
        self.knights.append(knight)
        knight.set_in_training_yard(True)
        knight.set_in_tavern(False)
        knight.set_at_round_table(False)

    def add_knight_to_tavern(self, knight):
        """Move a specified Knight object to the tavern.

        :param Knight knight: The Knight object to move to the tavern.
        """
        self.knights.append(knight)
        knight.set_in_tavern(True)
        knight.set_in_training_yard(False)
        knight.set_at_round_table(False)

    def add_knight_to_round_table(self, knight):
        """Move a specified Knight object to the round table.

        :param Knight knight: The Knight object to move to the round table.
        """
        self.knights.append(knight)
        knight.set_at_round_table(True)
        knight.set_in_tavern(False)
        knight.set_in_training_yard(False)

    def process(self):
        """Apply the logic for modifying the properties of each Knight."""
        for knight in self.knights:
            if knight.is_in_tavern:
                knight.increment_stamina(1)
            else:
                knight.increment_stamina(-1)

            if knight.is_in_training_yard and knight.stamina > 0:
                knight.increment_xp(1)

            if knight.is_at_round_table:
                knight.round_table_counter += 1

    def grant_bonus_xp(self):
        """Apply the bonus XP logic for each Knight."""
        bonus_knights = 0
        for knight in self.knights:
            if knight.xp >= 3:
                bonus_knights += 1

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
    # Initialize a new Codalot object.
    codalot = Codalot()

    # Create 6 new Knight objects to add to codalot.
    knights = []
    for i in range(codalot.num_of_knights):
        knights.append(Knight())
    knights.append(KingArthur())

    # Start the main event loop.
    random = Random()
    for _ in range(codalot.days_to_run):
        for _ in range(24):
            codalot.clear_knights()
            for knight in knights:
                random_val = random.randint(0, 2)
                if random_val == 0:
                    codalot.add_knight_to_training_yard(knight)
                elif random_val == 1:
                    codalot.add_knight_to_tavern(knight)
                elif random_val == 2:
                    codalot.add_knight_to_round_table(knight)
            codalot.process()
        for knight in knights:
            if (knight.round_table_counter < 3 or knight.stamina < 0) and not isinstance(knight, KingArthur):
                knight.xp = 0
    codalot.grant_bonus_xp()

    # Apply bonus XP at the end of the day.
    total_xp = 0
    for knight in knights:
        # Don't count King Arthur's XP with the rest of the knights.
        if isinstance(knight, KingArthur):
            continue
        total_xp += knight.xp

    print("Total XP earned by all " + str(len(knights) - 1) + " knights: " + str(total_xp))
    print("XP earned by King Arthur: " + str(knights[-1].xp))
