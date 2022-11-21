"""
CP1404 Practical
By: Rory Reid
UnreliableCar class tests

The point to an UnreliableCar is that it randomly does not always drive.
So, these tests run several times in order to see that randomness.
We expect the good car (high reliability) to drive more often than the bad car.
"""

from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars"""

    great_car = UnreliableCar("Great", 100, 90)
    terrible_car = UnreliableCar("Terrible", 100, 5)

    for i in range(1, 6):
        print(f"Attempting to drive {i}km:")
        print(f"{great_car.name:12} drove {great_car.drive(i):2}km")
        print(f"{terrible_car.name:12} drove {terrible_car.drive(i):2}km")

    print(great_car)
    print(terrible_car)


main()
