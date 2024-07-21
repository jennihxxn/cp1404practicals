import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)

def display_quick_picks(quick_picks):
    for pick in quick_picks:
        print(" ".join("{:2d}".format(number) for number in pick))

def main():
    num_quick_picks = int(input("How many quick picks? "))
    quick_picks = [generate_quick_pick() for _ in range(num_quick_picks)]
    display_quick_picks(quick_picks)

main()