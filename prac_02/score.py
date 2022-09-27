"""
CP1404 - Practical score.py
updated with function
Program to determine score status
The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent;
50 or more is a pass;
below 50 is bad.
"""

import random


def main():
    """main function determine score results"""
    score = float(input("Enter score: "))
    print(determine_valid_score(score))
    print(determine_valid_score(random.randint(0, 100)))


def determine_valid_score(score):
    """check if score is valid"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
