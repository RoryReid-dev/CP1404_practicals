"""
CP1404/CP5632 Practical
project management main program
"""

import datetime
from operator import attrgetter
from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
       "- (A)dd new project\n- (U)pdate project\n- (Q)uit "
FILENAME = "projects.txt"


def main():
    """main function for project management programme"""
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
            display_projects(projects)
        elif choice == "F":
            filter_date = input("Show projects that start after date (dd/mm/yy): ")
            display_filtered_projects(projects, filter_date)
        elif choice == "A":
            print("A")
        elif choice == "U":
            display_projects(projects)
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def display_filtered_projects(projects, filter_date):
    """Displays projects after inputted filter date """
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    filtered_projects.sort(key=attrgetter("start_date"))
    for project in filtered_projects:
        print(project)


def display_projects(projects):
    """Displays numbered list of projects."""
    for i, project in enumerate(projects):
        print(i, project)


def display_project_status(projects):
    """Displays projects split in completed incomplete and ordered priority."""
    print("Incomplete projects:")
    for project in sorted(projects):
        if not project.is_complete():
            print(" ", project)
    print("Completed projects:")
    for project in sorted(projects):
        if project.is_complete():
            print(" ", project)


def update_project(projects):
    """update completion and priority for projects """
    project_index = int(input("Project choice: "))
    project = projects[project_index]
    print(project)
    updated_completion = int(input("New Percentage: "))
    updated_priority = int(input("New Priority: "))
    project.completion_percentage = updated_completion
    project.priority = updated_priority


def load_file(projects, file):
    """Loads projects.txt."""
    with open(file, "r") as in_file:
        in_file.readline()  # Reads the header line
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)


def save_file(projects, file):
    """Saves projects to projects.txt"""
    with open(file, "w") as out_file:
        # Add headers to file
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(project.name, project.start_date, project.priority, project.cost_estimate, project.completion,
                  file=out_file, sep="\t")


main()
