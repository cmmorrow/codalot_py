"""This module hosts tests for Codealot."""

from random import Random

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
    codalot.process()

    assert codalot.calculate_earned_xp() == 0

    codalot.set_knight(0, KnightLocation.TRAINING_YARD)
    codalot.set_knight(6, KnightLocation.TRAINING_YARD)
    codalot.set_knight(7, KnightLocation.TRAINING_YARD)
    codalot.process()

    assert codalot.calculate_earned_xp() == 3
    assert codalot.knights[3].stamina < 0


def test_bonus_xp():
    """Test the bonus XP logic."""
    codalot = FixtureTestalot()

    # Set the even index Knights in the tavern and the odd index Knights in the training yard.
    for i in range(codalot.num_of_knights):
        if i % 2 == 0:
            codalot.set_knight(i, KnightLocation.TAVERN)
        else:
            codalot.set_knight(i, KnightLocation.TRAINING_YARD)

    # Process to increment stamina.
    for _ in range(4):
        codalot.process()

    # Switch Knights from the training yard to the tavern and vice versa.
    for i in range(codalot.num_of_knights):
        if i % 2 == 0:
            codalot.set_knight(i, KnightLocation.TRAINING_YARD)
        else:
            codalot.set_knight(i, KnightLocation.TAVERN)

    # Process again to generate XP.
    for _ in range(4):
        codalot.process()

    # Apply the XP bonuses.
    codalot.grant_bonus_xp()
    assert codalot.calculate_earned_xp() == 138


def test_run_five_days():
    """Test the case where Codalot runs for 5 days."""
    codalot = FixtureTestalot()
    random = Random(1)

    def run():
        for _ in range(codalot.days_to_run):
            for i in range(codalot.days_to_run * 24):
                for k in range(len(codalot.knights)):
                    random_val = random.randint(0, 2)
                    if random_val == 0:
                        codalot.set_knight(k, KnightLocation.TRAINING_YARD)
                    elif random_val == 1:
                        codalot.set_knight(k, KnightLocation.TAVERN)
                    elif random_val == 2:
                        codalot.set_knight(k, KnightLocation.ROUND_TABLE)
                codalot.process()
    run()
    assert codalot.calculate_earned_xp() == 3
    codalot.days_to_run = 7
    run()
    assert codalot.calculate_earned_xp() == 3
