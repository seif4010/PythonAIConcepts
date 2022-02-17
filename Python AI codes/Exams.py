# candy store that has 8 candies
# when it reaches 50% it should tell the store owner to fill them
# using Object oriented within it
import random


class Candies(object):
    def __init__(self, name, CandieType):
        self.name = name
        self.CandieType = CandieType


class store:
    def __init__(self) -> None:
        print("")
