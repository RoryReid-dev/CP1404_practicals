"""
CP1404 - Menu
pseudocode
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU_PROMPT = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU_PROMPT)
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU_PROMPT)
    menu_choice = input(">>> ").upper()
print("Finished")
