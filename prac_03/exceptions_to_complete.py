"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit loop as valid input has been accepted
    except ValueError: # Exception to handle incorrect input, anything that isn't an integer
        print("Please enter a valid integer.")
print("Valid result is:", result)
