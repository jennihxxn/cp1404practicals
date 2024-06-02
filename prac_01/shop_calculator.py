"""
Pseudocode for shop calculator

get number of items from user
    set total_price = 0

    GET number_of_items
    For number_of_items times:
        GET item_price
        total_price = total_price + item_price

    If total_price > 100:
        total_price = total_price * 0.9  # Apply 10% discount

    PRINT "The total price is ${total_price}"
"""

num_items = int(input("Number of items: "))

while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

total_price = 0

for item in range(num_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {num_items} items is ${total_price:.2f}")