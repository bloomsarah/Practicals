"""Guitar class to store one guitar with several fields of information"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2018 - self.year
        return "Age: {} years".format(age)

    def is_vintage(self):
        if age >= 50:
            vintage = True
        else:
            vintage = False
        return "Vintage: {}".format(vintage)
