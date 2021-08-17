#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# Fibonacci Series

import sys


# Using recursion
def fibonacci1(num):
    if num <= 1:
        return num
    else:
        return fibonacci1(num - 1) + fibonacci1(num - 2)


# Using yield keyword
def fibonacci2(num):
    a, b, count = 0, 1, 1
    while True:
        if count > num:
            return
        else:
            yield a
            a, b = b, a + b
            count += 1


if __name__ == "__main__":
    num_terms = int(input("How many terms?\n"))

    for i in range(num_terms):
        print(f"{fibonacci1(i)} ", end='')
    else:
        print()

    f = fibonacci2(num_terms)  # create a generator
    while True:
        try:
            print(f"{next(f)} ", end='')
        except StopIteration:
            sys.exit()
