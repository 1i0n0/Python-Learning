#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Determine the least common multiple of two positive integer numbers.
import sys


def lcm(num1, num2):
    _lcm = max(num1, num2)

    while True:
        if _lcm % num1 == 0 and _lcm % num2 == 0:
            break
        _lcm += 1

    return _lcm


if __name__ == "__main__":
    try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))

        assert number1 > 0
        assert number2 > 0
    except ValueError:
        print("Please enter two non-zero positive integers.")
        sys.exit(1)
    except AssertionError:
        print("Please enter two non-zero positive integers.")
        sys.exit(1)

    print("The least common multiple of {} and {} is {}"
          .format(number1, number2, lcm(number1, number2)))
