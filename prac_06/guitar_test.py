from guitar import Guitar
import datetime


def test_guitar_methods():
    """Test the methods of the Guitar class."""

    # Get the current year for age calculations
    current_year = datetime.datetime.now().year

    # Test guitar 1: Gibson L-5 CES
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar1_age = current_year - 1922
    print(f"{guitar1.name} get_age() - Expected {guitar1_age}. Got {guitar1.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")

    # Test guitar 2: Another Guitar
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)
    guitar2_age = current_year - 2013
    print(f"{guitar2.name} get_age() - Expected {guitar2_age}. Got {guitar2.get_age()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

    # Test guitar 3: 50-year old guitar (for testing the boundary of vintage)
    vintage_year = current_year - 50
    guitar3 = Guitar("50-year old guitar", vintage_year, 2000.00)
    print(f"{guitar3.name} is_vintage() - Expected True. Got {guitar3.is_vintage()}")


def main():
    """Run the guitar testing program."""
    print("Guitar class tests:")
    test_guitar_methods()


if __name__ == "__main__":
    main()
