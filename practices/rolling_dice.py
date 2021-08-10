#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# Create two dice objects and roll them

import random


class Dice:
    __max = 6   # maximum face value
    faceValue = 0   # current value showing on the dice

    # Set the initial face value
    def __init__(self):
        self.faceValue = 1

    # Roll the dice
    def roll(self):
        self.faceValue = random.randint(1, self.__max)

    # Get the current face value
    def get_face_value(self):
        return self.faceValue


if __name__ == "__main__":
    sum = lambda x, y: x + y    # a lambda expression
    dice1 = Dice()
    dice2 = Dice()

    dice1.roll()
    dice2.roll()
    v1 = dice1.get_face_value()
    v2 = dice2.get_face_value()
    print("Dice One: {0}, Dice Two: {1}".format(v1, v2))
    print("Sum: {0}".format(sum(v1, v2)))
