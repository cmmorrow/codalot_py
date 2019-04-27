"""This module hosts the Codalot test fixture."""

from codealot.main import Codalot, Knight, NUM_OF_KNIGHTS
from test.KnightLocation import KnightLocation


class Testalot(object):
    """Create a Codalot abstract class for testing."""

    def set_knight(self, idx, location):
        """Set a Knight's state for testing.

        :param int idx: The index of a Knight object in a list of knights.
        :param KnightLocation location: The location of the Knight object to set.
        """
        raise NotImplementedError

    def calculate_earned_xp(self):
        raise NotImplementedError


class TestalotFixture(Codalot, Testalot):
    """The Codalot test fixture."""

    knights = []

    def __init__(self):
        """Initialize a new fixture object."""
        super(Codalot, self).__init__()
        for _ in range(NUM_OF_KNIGHTS):
            self.knights.append(Knight())

    def set_knight(self, idx, location):
        """Set a Knight's state for testing.

        :param int idx: The index of a Knight object in a list of knights.
        :param KnightLocation location: The location of the Knight object to set.
        """
        knight = self.knights[idx]
        if location == KnightLocation.TAVERN:
            knight.set_in_tavern(True)
        elif location == KnightLocation.TRAINING_YARD:
            knight.set_in_training_yard(True)

    def calculate_earned_xp(self):
        """Add up the XP of all Knights.

        :return: The sum of the XP of all Knights.
        """
        total = 0
        for knight in self.knights:
            total += knight.xp
        return total
