import random

def roll_dice(sides=6):
    """Roll a dice with specified sides."""
    return random.randint(1, sides)

def roll_multiple(count=1, sides=6):
    """Roll multiple dice."""
    return [roll_dice(sides) for _ in range(count)]

if __name__ == "__main__":
    print(f"Single roll: {roll_dice()}")
    print(f"Multiple rolls: {roll_multiple(3)}")