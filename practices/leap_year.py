#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Leap year: a year of 366 days instead of 365 with February having 29 days instead of 28

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


if __name__ == "__main__":
    y = int(input("Enter a year: \n"))

    if is_leap_year(y):
        print(f"{y} IS a leap year.")
    else:
        print(f"{y} IS NOT a leap year.")
