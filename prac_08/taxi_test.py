from prac_08.taxi import Taxi


def main():
    """Test for the Taxi class"""
    prius = Taxi("Prius 1", 100)
    prius.drive(40)
    print(prius)
    print("Fare = $", prius.get_fare())
    prius.start_fare()
    print(prius)
    print("Fare = $", prius.get_fare())


main()