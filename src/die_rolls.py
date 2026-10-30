import random

def roll_dice(sides: int = 6) -> int:
    """Roll a single die with a given number of sides."""
    if sides < 1:
        raise ValueError("A die must have at least 1 side.")
    return random.randint(1, sides)

def roll_multiple(num: int, sides: int = 6) -> list:
    """Roll multiple dice and return a list of results."""
    if num < 1:
        raise ValueError("Must roll at least 1 die.")
    return [roll_dice(sides) for _ in range(num)]