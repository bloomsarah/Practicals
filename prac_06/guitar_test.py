"""CP1404 Class Practical guitars class test file."""


from prac_06.guitar import Guitar

CURRENT_YEAR = 2018


def main():

    gibson = Guitar('Gibson L-5 CES', 1922, 16035.40)
    other = Guitar('Another Guitar', 2012, 1000.00)
    fifty_year_guitar = Guitar('50 Year Old Guitar', 1968, 1234.90)

    print("{} get_age() - Expected {}. Got {}".format(gibson.name, 96, gibson.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, gibson.is_vintage()))
    print()

    print("{} get_age() - Expected {}. Got {}".format(other.name, 6, other.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))
    print()

    print("{} get_age() - Expected {}. Got {}".format(fifty_year_guitar.name, 50, fifty_year_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(fifty_year_guitar.name, True, fifty_year_guitar.is_vintage()))
    print()


main()
