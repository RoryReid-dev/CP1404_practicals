"""
CP1404 Practical
By: Rory Reid
SilverServiceTaxi class tests
"""


from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Taxi", 100, 6)
    taxi.drive(14)
    print(taxi)
    print(taxi.get_fare())


main()
