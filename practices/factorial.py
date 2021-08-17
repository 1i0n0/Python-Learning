#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# Find factorial of number
import sys
import math  # another solution using math.factorial


# Find factorial of number using recursion
def my_factorial(num):
    if num < 0:
        print("It is not a positive integer.")
        sys.exit(1)
    elif num == 0:
        return 1
    else:
        return num * my_factorial(num - 1)


if __name__ == "__main__":
    number = int(input("Enter a positive integer: \n"))

    result = my_factorial(number)
    assert result == math.factorial(number)
    if result:
        print(f"The factorial of {number} is {result}.")
