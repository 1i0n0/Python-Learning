#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Determine the greatest common divisor of two positive integer numbers.
import sys


def gcd(num1, num2):
    upper_limit = min(num1, num2)
    hcf = None  # highest common factor

    for i in range(1, upper_limit + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf


if __name__ == "__main__":
    try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))

        assert number1 >= 0
        assert number2 >= 0
    except ValueError:
        print("Please enter two positive integer numbers.")
        sys.exit(1)
    except AssertionError:
        print("Please enter two positive integer numbers.")
        sys.exit(1)

    print("The greatest common divisor of {} and {} is {}"
          .format(number1, number2, gcd(number1, number2)))
