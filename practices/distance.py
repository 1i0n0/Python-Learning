#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Compute the distance between the two points
import sys
from math import sqrt


def calc_distance():
    try:
        # (x1, y1)
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))

        # (x2, y2)
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))

        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print("Distance: {0:.2f}".format(distance))
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    calc_distance()
