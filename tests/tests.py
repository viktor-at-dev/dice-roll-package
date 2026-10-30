from src import die_rolls
def roll_test():
    result =  die_rolls.roll_dice(1)
    assert 1 <= result <= 6

def test_roll_multiple():
    results = die_rolls.roll_multiple(3, 6)
    assert len(results) == 3
    assert all(1 <= r <= 6 for r in results)