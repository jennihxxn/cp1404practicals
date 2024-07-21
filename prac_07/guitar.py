import datetime

class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar."""
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50 or more years old)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year."""
        return self.year < other.year
