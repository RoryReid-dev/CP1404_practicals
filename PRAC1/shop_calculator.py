"""
CP1404 - Practical shop_calculator
Example
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
"""

# first iteration without error checking
total = 0
number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total += item_price
if total > 100:
    total *= 0.9
print(f"Total price for {number_of_items} items is ${total:.2f}")

# Second iteration with error checking
total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total += item_price
if total > 100:
    total *= 0.9
print(f"Total price for {number_of_items} items is ${total:.2f}")
