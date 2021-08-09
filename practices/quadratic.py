#!/usr/bin/python3
# -*- coding = UTF-8 -*-
import sys
from math import pow, sqrt


# Determine the roots of a quadratic equation
def quadratic_equation():
    try:
        a = int(input("Enter the coefficient of x^2: "))
        b = int(input("Enter the coefficient of x: "))
        c = int(input("Enter the constant: "))

        if a == 0:
            print("This is not a quadratic equation.")
            sys.exit(1)

        # Use the quadratic formula to compute the roots
        discriminant = pow(b, 2) - (4 * a * c)

        # For a positive discriminant
        if discriminant > 0:
            root1 = ((-1 * b) + sqrt(discriminant)) / (2 * a)
            root2 = ((-1 * b) - sqrt(discriminant)) / (2 * a)
            print("Root #1: {0}".format(root1))
            print("Root #2: {0}".format(root2))
    except ValueError as v_error:
        print(v_error)
        sys.exit(2)
    except ZeroDivisionError as zd_error:
        print(zd_error)
        sys.exit(3)


if __name__ == "__main__":
    quadratic_equation()
