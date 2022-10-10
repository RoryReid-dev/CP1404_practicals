"""
CP1404/CP5632 Practical
Lottery Quick Picks program
"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_TO_DISPLAY = 6


def main():
    """Lottery quick pick generator"""
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 0:
        print("Please enter a number above 0")
        number_of_picks = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(number_of_picks)
    display_quick_picks(quick_picks)


def generate_quick_picks(number_of_picks):
    """Generate x quick picks"""
    quick_picks = []
    for i in range(number_of_picks):
        picks = []
        for j in range(NUMBERS_TO_DISPLAY):
            number = random.randrange(MINIMUM, MAXIMUM + 1)
            while number in picks:
                # Generate new number if it is already in the list
                number = random.randrange(MINIMUM, MAXIMUM + 1)
            picks.append(number)
        quick_picks.append(picks)
    return quick_picks


def display_quick_picks(quick_picks):
    """Display quick pick data neatly."""
    for quick_pick in quick_picks:
        quick_pick.sort()
        for number in quick_pick:
            print(f"{number:2}", end=" ")
        print()


main()
