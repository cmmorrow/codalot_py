"""This module hosts tests for Codealot."""

from test.fixtures import FixtureTestalot
from test.KnightLocation import KnightLocation


def test_process():
    """Test the process logic to make sure it's working as expected."""
    codalot = FixtureTestalot()

    codalot.set_knight(0, KnightLocation.TAVERN)
    codalot.set_knight(1, KnightLocation.TAVERN)
    codalot.set_knight(2, KnightLocation.TRAINING_YARD)
    codalot.set_knight(3, KnightLocation.TRAINING_YARD)
    codalot.set_knight(4, KnightLocation.TRAINING_YARD)
    codalot.set_knight(5, KnightLocation.TRAINING_YARD)
    codalot.set_knight(6, KnightLocation.TAVERN)
    codalot.set_knight(7, KnightLocation.TAVERN)
    codalot.set_knight(8, KnightLocation.TRAINING_YARD)
    codalot.set_knight(9, KnightLocation.TRAINING_YARD)
    codalot.set_knight(10, KnightLocation.TRAINING_YARD)
    codalot.set_knight(11, KnightLocation.TRAINING_YARD)
    codalot.process()

    assert codalot.calculate_earned_xp() == 0

    codalot.knights[0].set_in_training_yard(True)
    codalot.knights[7].set_in_training_yard(True)
    codalot.process()

    assert codalot.calculate_earned_xp() == 2
