"""
CP1404/CP5632 Practical
Hex Colour
"""

colour_to_codes = {"Pine Green": "#01796f", "Pine Tree": "#2a2f23", "Pink": "#ffc0cb",
                   "Pink Pantone": "#d74894", "Pink Flamingo": "#fc74fd", "Pink Sherbet": "#f78fa7",
                   "Pistachio": "#93c572",
                   "Platinum": "#e5e4e2", "Black Coffee": "#3b2f2f", "Black Olive": "#3b3c36"}

colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    try:
        code = {colour.title(): code for colour, code in colour_to_codes.items()}
        print(f"The code for \"{colour_name}\" is {colour_to_codes.get(colour_name)}")
    except KeyError:
        print("Invalid colour entered.")
    colour_name = input("Enter colour name: ").title()
