"""
CP1404 Practical
By: Rory Reid
Band class
"""


class Band:
    """Band Class"""

    def __init__(self, name=""):
        """Initialise an instance of a band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """String representation of a band."""
        band = ','.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({band})"

    def add(self, musician):
        """Adds a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Get all band members to play their instruments."""
        for person in self.musicians:
            print(person.play())