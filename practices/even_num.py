#!/usr/bin/python3
# -*- coding: utf-8 -*-

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(input("Enter a number: \n"))

    if is_even(number):
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
