"""
Guitars basic program to test class
Estimate: 30 minutes
Actual:   35 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Main program for guitars"""
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    width = max([len(guitar.name) for guitar in guitars])
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, start=1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>{width}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No Guitars =( go buy a Gretsch White Falcon!")


main()
