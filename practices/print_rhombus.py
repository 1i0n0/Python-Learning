#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Print a rhombus shape using *

import sys

if __name__ == "__main__":
    length = int(input("Length of side: "))
    if length == 1:
        print("*")
        sys.exit()
    elif length < 1:
        print("Should greater than 0.")
        sys.exit(1)

    i = 0  # a counter

    # Top half
    for i in range(length * 2):
        if i % 2 == 0:
            continue
        stars = '*' * i
        print(stars.center(length * 2 - 1, ' '))

    # Bottom half
    while i > 1:
        i -= 2
        if i % 2 == 0:
            continue
        stars = '*' * i
        print(stars.center(length * 2 - 1, ' '))
