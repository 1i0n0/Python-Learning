#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def calc_perimeter(a, b, c):
    return a + b + c


def calc_area(a, b, c):
    s = calc_perimeter(a, b, c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


if __name__ == "__main__":
    try:
        print("What is the lengths of the sides of your triangle?")
        a = float(input("Enter the length of the 1st side: "))
        b = float(input("Enter the length of the 2nd side: "))
        c = float(input("Enter the length of the 3rd side: "))
    except ValueError:
        print("Please enter 3 numbers.")
    else:
        if not is_triangle(a, b, c):
            print("It is not a triangle.")
            sys.exit(1)

        perimeter = calc_perimeter(a, b, c)
        area = calc_area(a, b, c)
        print("perimeter = {0:.2f}, area = {1:.2f}".format(perimeter, area))
