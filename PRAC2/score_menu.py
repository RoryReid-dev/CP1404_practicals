"""
CP1404 - score with menu
get a valid score (must be 0-100 inclusive)
print result (copy or import your function from score.py)
print stars (this should print as many stars as the score)
quit
"""

MENU_PROMPT = "(G)et score\n(P)rint result\n(D)isplay stars\n(Q)uit"


def main():
    """score calculator with menu"""
    score = 0
    print(MENU_PROMPT)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_valid_score(score))
        elif choice == "D":
            # TODO
            pass
        else:
            print("Invalid choice")
        print(MENU_PROMPT)
        choice = input(">>>").upper()


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


def get_valid_score():
    """get user input and validate against thresholds"""
    score = float(input("Enter score (0 - 100): "))
    while score < 0 or score > 100:
        print("Invalid Score, try again enter a number between 0 - 100")
        score = float(input("Enter score (0 - 100): "))
    return score


main()
