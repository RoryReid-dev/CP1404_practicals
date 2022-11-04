"""
My guitars
Write a program to read all of these guitars and store them in a list of Guitar objects, using the class that you wrote recently.
Display these using a loop.
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main program for guitars"""
    guitars = []
    load_file(guitars)
    display_guitars(guitars)


def display_guitars(guitars):
    """Display guitars that are in list added by user or imported from CSV """
    width = max([len(guitar.name) for guitar in guitars])
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, start=1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>{width}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No Guitars =( go buy a Gretsch White Falcon!")


def load_file(guitars):
    """Guitar file reader version using the csv module."""
    in_file = open(FILENAME, 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        row[1] = int(row[1])
        row[2] = float(row[2])
        guitar = Guitar(row[0], int(row[1]), float(row[2]))
        guitars.append(guitar)
    in_file.close()


main()
