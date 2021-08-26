#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Determine whether the given number is Armstrong number or not.
# An Armstrong number is a number that is the sum of its own digits
# each raised to the power of the number of digits.

def is_armstrong_num(num):
    digits = str(num)
    num_digits = len(digits)
    _sum = 0

    for i in range(num_digits):
        _sum += pow(int(digits[i]), num_digits)

    if _sum == num:
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    if is_armstrong_num(number):
        print(f"{number} IS an Armstrong number.")
    else:
        print(f"{number} IS NOT an Armstrong number.")

    '''
    # Print all Armstrong numbers between 1 and 500
    for i in range(1,500):
        if is_armstrong_num(i):
            print(i)
    '''
