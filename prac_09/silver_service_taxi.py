"""
CP1404 Practical
By: Rory Reid
SilverServiceTaxi class, derived from Taxi
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flag fall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare"""
        return self.flagfall + super().get_fare()
