"""
Guitar Class file
Estimate: 30 minutes
Actual:   35 minutes
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """basic class for guitar information"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Method to return if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
