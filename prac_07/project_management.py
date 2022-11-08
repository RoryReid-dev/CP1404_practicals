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
            projects = get_user_file()
        elif choice == "S":
            user_save_file = get_valid_string("Enter File name to save: ")
            save_file(projects, user_save_file)
        elif choice == "D":
            display_project_status(projects)
        elif choice == "F":
            display_filtered_projects(projects)
        elif choice == "A":
            print("Let's add a new project")
            add_project(projects)
        elif choice == "U":
            display_projects(projects)
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_file(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def get_valid_date(prompt):
    """Gets valid date from user."""
    is_valid_date = False
    while not is_valid_date:
        try:
            filter_date = input(prompt)
            date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Enter a valid date in format DD/MM/YYYY")
    return date


def get_valid_string(prompt):
    """Get a valid input that is not blank using exception handling"""
    user_input = input(prompt)
    while user_input == "":
        print("Input can not be blank")
        user_input = input(prompt)
    return user_input


def get_valid_input(default_value, prompt, low, high):
    """Get integer between low and high or return value if no user input."""
    is_valid = False
    while not is_valid:
        try:
            user_input = input(prompt)
            if user_input == "":
                user_input = default_value
                return user_input
                is_valid = True
            if int(user_input) < low or int(user_input) > high:
                print(f"Please enter a number from {low} - {high}")
            else:
                user_input = int(user_input)
                return user_input
                is_valid = True
        except ValueError:
            print("Must be a number or enter blank value to keep the same")


def get_valid_number(prompt, low, high):
    """Get a valid integer above 0 using exception handling"""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            while number < low or number > high:
                print(f"Invalid number. Please enter a number between {low} - {high}.")
                number = int(input(prompt))
            is_valid_number = True
        except ValueError:
            print(f"Invalid number. Please enter a number between {low} - {high}.")
    return number  # no problem with potential undefined variable


def get_valid_float(prompt):
    """Get a valid float above 0 using exception handling"""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = float(input(prompt))
            while number < 0:
                print("Number must be >= 1")
                number = float(input(prompt))
            is_valid_number = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number  # no problem with potential undefined variable


def add_project(projects):
    name = get_valid_string("Name: ")
    date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ", 1, 20)
    cost = get_valid_float("Cost estimate: $")
    completion = get_valid_number("Percent complete: ", 0, 100)
    new_project = Project(name, date, priority, cost, completion)
    projects.append(new_project)


def display_filtered_projects(projects):
    """Displays projects after inputted filter date """
    filter_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
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
    project_index = get_valid_number("Project choice: ", 0, len(projects) - 1)  # Get true index with -1
    project = projects[project_index]
    print(project)
    updated_completion = get_valid_input(project.completion, "New Percentage: ", 0, 100)
    updated_priority = get_valid_input(project.priority, "New Priority: ", 0, 10)
    project.completion = updated_completion
    project.priority = updated_priority


def get_user_file():
    """Gets user entered valid file to load."""
    loaded_projects = []
    valid_input = False
    while not valid_input:
        try:
            loaded_project_file = input("Enter file you wish to load: ")
            load_file(loaded_projects, loaded_project_file)
            valid_input = True
        except FileNotFoundError:
            print(f"Unable to find file {loaded_project_file}")
    return loaded_projects


def load_file(projects, file):
    """Loads projects.txt."""
    with open(file, "r") as in_file:
        in_file.readline()  # Reads the header line
        for line in in_file:
            section = line.strip().split("\t")
            project = Project(section[0], section[1], int(section[2]), float(section[3]), int(section[4]))
            project.start_date = datetime.datetime.strptime(project.start_date,
                                                            "%d/%m/%Y").date()  # convert string to date
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
