"""
CP1404/CP5632 - practical_3 files.py
1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
2. Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
3. Create a text file called numbers.txt and save it in your prac_02 directory.
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt",
reads only the first two numbers and adds them together then prints the result, which should be... 59.
4. Now write a fourth block of code that prints the total for all lines in numbers.txt,
or a file with any number of numbers.
"""

name = input("Please enter you name: ").title()
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

