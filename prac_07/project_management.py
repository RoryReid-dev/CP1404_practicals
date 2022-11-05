"""
CP1404/CP5632 Practical
project management main program
"""

import datetime
from operator import attrgetter
from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "
FILENAME = "projects.txt"


def main():
    projects = []
    load_file(projects, FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            user_load_file = input("Enter file name to load: ")
            load_file(projects, user_load_file)
        elif choice == "S":
            user_save_file = input("Enter File name to save: ")
            save_file(projects, user_save_file)
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


def load_file(projects, file):
    """Loads projects.txt."""
    with open(FILENAME, "r") as in_file:
        in_file.readline()  # Reads the header line
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)


def save_file(projects, file):
    """Saves projects to projects.txt"""
    with open(FILENAME, "w") as out_file:
        # Add headers to file
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(project.name, project.start_date, project.priority, project.cost_estimate, project.completion,
                  file=out_file, sep="\t")


main()
