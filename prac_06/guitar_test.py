from guitar import Guitar
import datetime

def main():
    current_year = datetime.datetime.now().year

    # Create guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)
    guitar3 = Guitar("50-year old guitar", current_year - 50, 2000.00)

    # Test get_age() method
    print(f"{guitar1.name} get_age() - Expected {current_year - 1922}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {current_year - 2013}. Got {guitar2.get_age()}")

    # Test is_vintage() method
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
    print(f"{guitar3.name} is_vintage() - Expected True. Got {guitar3.is_vintage()}")

if __name__ == "__main__":
    main()