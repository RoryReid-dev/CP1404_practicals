"""
CP1404 Practical
By: Rory Reid
SilverServiceTaxi class tests
"""


from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"${taxi.get_fare():.2f}")


main()
