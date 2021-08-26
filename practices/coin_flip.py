#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Flip a coin

import random


class Coin:
    __head = 0
    __tail = 1
    __face = None

    # Set up the coin by flipping it initially
    def __init__(self):
        self.flip()

    # Flip the coin by randomly choosing a face value
    def flip(self):
        self.__face = random.choice([0, 1])

    # Return true if the current face of the coin is head
    def is_head(self):
        return self.__face == self.__head

    # Return the current face of the coin as a string
    def __str__(self):
        if self.is_head():
            face_name = "Head"
        else:
            face_name = "Tail"

        return face_name


# Create a Coin object, flip it, and print the result
if __name__ == "__main__":
    my_coin = Coin()

    my_coin.flip()

    print(my_coin)

    if my_coin.is_head():
        print("You win.")
    else:
        print("Better luck next time.")
