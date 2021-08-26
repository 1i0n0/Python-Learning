#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Reverse the digits of a integer

if __name__ == "__main__":
    num = int(input("Enter a integer: \n"))
    sign = 1  # used to take the sign of the number

    # Remove the sign
    if num < 0:
        sign = -1
        num = abs(num)

    digits = str(num)
    digits = digits[-1::-1]
    reverse_num = sign * int(digits)

    print(reverse_num)
