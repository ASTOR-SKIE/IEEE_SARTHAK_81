import random

print("🎲 Dice Roller")

while True:
    input("Press Enter to roll the dice...")
    number = random.randint(1,6)
    print("You rolled:", number)

    again = input("Roll again? (yes/no): ")
    if again == "no":
        break