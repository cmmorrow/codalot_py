"""This module hosts the Codalot test fixture."""

from codealot.main import Codalot, Knight
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


class FixtureTestalot(Codalot, Testalot):
    """The Codalot test fixture."""

    def __init__(self):
        """Initialize a new fixture object."""
        super(FixtureTestalot, self).__init__()
        for _ in range(self.num_of_knights):
            self.knights.append(Knight())

    def set_knight(self, idx, location):
        """Set a Knight's state for testing.

        :param int idx: The index of a Knight object in a list of knights.
        :param KnightLocation location: The location of the Knight object to set.
        """
        knight = self.knights[idx]
        if location == KnightLocation.TAVERN:
            knight.set_in_tavern(True)
            knight.set_in_training_yard(False)
            knight.set_at_round_table(False)
        elif location == KnightLocation.TRAINING_YARD:
            knight.set_in_training_yard(True)
            knight.set_in_tavern(False)
            knight.set_at_round_table(False)
        elif location == KnightLocation.ROUND_TABLE:
            knight.set_at_round_table(True)
            knight.set_in_training_yard(False)
            knight.set_in_tavern(False)

    def calculate_earned_xp(self):
        """Add up the XP of all Knights.

        :return: The sum of the XP of all Knights.
        """
        total = 0
        for knight in self.knights:
            total += knight.xp
        return total
