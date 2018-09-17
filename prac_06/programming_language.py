"""CP1404 Practical 6: Programming Language Class."""


class ProgrammingLanguage:
    """Represent a Programming Language object"""

    def __init__(self, name="", typing="", reflection=True, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name.capitalize(),
                                                                           self.typing.capitalize(), self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        if typing.lower() == dynamic:
            dynamic_boolean = True
        else:
            dynamic_boolean = False
        return dynamic_boolean

