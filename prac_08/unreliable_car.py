from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialized case of Car that includes reliability float."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven