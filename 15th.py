import random

def roll_dice():
    total = 0
    while True:
        roll = random.randint(1, 6)
        total += roll
        print(f"You rolled a {roll}. Total: {total}")
        choice = input("Roll again? (y/n): ")
        if choice.lower() != 'y':
            break

roll_dice()
