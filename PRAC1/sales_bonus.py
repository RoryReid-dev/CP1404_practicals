"""
CP1404 - Practical 1. Sales Bonus
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Without loop
sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * .1
else:
    bonus = sales * .15
print(f"Bonus is ${bonus:.0f}")

# With Loop
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * .1
    else:
        bonus = sales * .15
    print(f"Bonus is ${bonus:.0f}")
    sales = float(input("Enter sales: $"))
