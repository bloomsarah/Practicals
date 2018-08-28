"""
Generate program that asks for number of quick picks
print that number of lines, with 6 numbers per line
numbers must be sorted and between 1 and 45
"""

import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():

    number_of_picks = int(input("Enter number of picks: "))
    while number_of_picks < 0:
        print("Invalid number of picks.")
        number_of_picks = int(input("Enter number of picks: "))

    for i in range(number_of_picks):
        pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in pick:
                number = random.randint(MIN, MAX)
            pick.append(number)
        pick.sort()
        print(" ".join("{:2}".format(number) for number in pick))


main()
