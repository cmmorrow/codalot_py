"""This module hosts tests for Codealot."""

from test.fixtures import TestalotFixture
from test.KnightLocation import KnightLocation

codalot = TestalotFixture()

codalot.set_knight(0, KnightLocation.TAVERN)
codalot.set_knight(1, KnightLocation.TAVERN)
codalot.set_knight(2, KnightLocation.TRAINING_YARD)
codalot.set_knight(3, KnightLocation.TRAINING_YARD)
codalot.set_knight(4, KnightLocation.TRAINING_YARD)
codalot.set_knight(5, KnightLocation.TRAINING_YARD)
codalot.process()

assert (codalot.calculate_earned_xp() == 4)
