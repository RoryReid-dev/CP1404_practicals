"""
CP1404/CP5632 Practical
Using lists exercises
1. Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers
2. Ask the user for their username. If the username is in the above list of authorised users, print "Access granted",
otherwise print "Access denied"
"""

# 1. Basic List operations
numbers = []

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user = input("Username: ")
if user in usernames:
    print("Access granted")
else:
    print("Access denied")
