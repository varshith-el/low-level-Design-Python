# dice.py
import random

class Dice:
    def __init__(self, minValue, maxValue, currentValue):
        self._minValue = minValue
        self._maxValue = maxValue
        self._currentValue = currentValue
    #roll the dice selects random number
    def roll(self):
        return random.randint(self._minValue, self._maxValue)

