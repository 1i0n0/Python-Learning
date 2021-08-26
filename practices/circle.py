#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import pi


def calc_circumference(r):
    return 2.0 * pi * r


def calc_area(r):
    return pi * r ** 2


if __name__ == "__main__":
    try:
        radius = float(input("What is the radius of your circle?\n"))
    except ValueError:
        print("Please enter a number.")
    else:
        assert radius > 0
        circumference = calc_circumference(radius)
        area = calc_area(radius)
        print("circumference = {0:.2f}, area = {1:.2f}".format(circumference, area))
