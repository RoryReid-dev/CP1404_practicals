"""
CP1404 - Practical Password_stars
write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum
length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.
"""

MIN_LENGTH = 3

password = input("Please enter a valid password (minimum 3 characters in length): ")
while len(password) < MIN_LENGTH:
    print("Password is not valid")
    password = input("Please enter a valid password (minimum 3 characters in length): ")
for i in range(len(password)):
    print("*", end=" ")
