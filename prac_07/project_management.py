"""
CP1404/CP5632 Practical
project management main program
"""

import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("L")
        elif choice == "S":
            print("S")
        elif choice == "D":
            print("D")
        elif choice == "F":
            print("F")
        elif choice == "A":
            print("A")
        elif choice == "U":
            print("U")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


main()
