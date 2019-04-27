"""This module hosts tests for Codealot."""

from test.BasicCodalot import BasicCodalot
from test.KnightPosition import KnightPosition

codalot = BasicCodalot()

codalot.set_knight(0, KnightPosition.TAVERN)
codalot.set_knight(1, KnightPosition.TAVERN)
codalot.set_knight(2, KnightPosition.TRAINING_YARD)
codalot.set_knight(3, KnightPosition.TRAINING_YARD)
codalot.set_knight(4, KnightPosition.TRAINING_YARD)
codalot.set_knight(5, KnightPosition.TRAINING_YARD)
codalot.process()

assert (codalot.calculate_earned_xp() == 4)
