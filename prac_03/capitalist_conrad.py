"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# Constants
STARTING_PRICE = 10.00
MIN_PRICE = 1.00  # Changed: Minimum price is $1
MAX_PRICE = 100.00  # Changed: Maximum price is $100
INCREASE_MIN = 0
INCREASE_MAX = 17.5  # Changed: Maximum increase is 17.5%
DECREASE_MIN = 0
DECREASE_MAX = 5
FILENAME = "stock_prices.txt"

def simulate_stock_price():
    price = STARTING_PRICE
    number_of_days = 0

    with open(FILENAME, 'w') as out_file:
        print(f"Starting price: ${price:.2f}", file=out_file)

        while MIN_PRICE <= price <= MAX_PRICE:
            number_of_days += 1
            if random.randint(1, 2) == 1:  # 50% chance of increase
                change_percent = random.uniform(INCREASE_MIN, INCREASE_MAX) / 100
            else:  # 50% chance of decrease
                change_percent = -random.uniform(DECREASE_MIN, DECREASE_MAX) / 100

            price *= (1 + change_percent)
            print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

    print(f"\nSimulation ended after {number_of_days} days.")

simulate_stock_price()
