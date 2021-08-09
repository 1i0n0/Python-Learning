#!/usr/bin/python3
# -*- coding = UTF-8 -*-
import sys
import re

base = 32
conversion_factor = 9.0 / 5.0
degree_symbol = '\xB0'


# Computes the Fahrenheit (F) equivalent of a specific Celsius (C)
# F = (9 / 5) * C + 32
def celsius2fahrenheit(c):
    return conversion_factor * c + 32


# Computes the Celsius (C) equivalent of a specific Fahrenheit (F)
# C = (F - 32) / (9 / 5)
def fahrenheit2celsius(f):
    return (f - 32) / conversion_factor


if __name__ == "__main__":
    # Get a temperature like 24C or 75.2F
    temp = input("Please enter a temperature (end with C/F): \n")

    # Call sys.exit() if it is not a temperature
    temp = temp.strip()
    if not re.match('[0-9]+(\.[0-9]+)*[C|F]$', temp, re.I):
        print("Please enter a temperature, e.g. 24C, 75.2F")
        sys.exit(1)

    # Convert the temperature
    if temp[-1] in ['C', 'c']:
        # degrees Celsius to degrees Fahrenheit
        celsius_temp = float(temp[0:-1])
        fahrenheit_temp = celsius2fahrenheit(celsius_temp)
        print("Celsius Temperature: {0:.1f}{1}C".format(celsius_temp, degree_symbol))
        print("Fahrenheit Equivalent: {0:.1f}{1}F".format(fahrenheit_temp, degree_symbol))
    elif temp[-1] in ['F', 'f']:
        # degrees Fahrenheit to degrees Celsius
        fahrenheit_temp = float(temp[0:-1])
        celsius_temp = fahrenheit2celsius(fahrenheit_temp)
        print("Fahrenheit Temperature: {0:.1f}{1}F".format(fahrenheit_temp, degree_symbol))
        print("Celsius Equivalent: {0:.1f}{1}C".format(celsius_temp, degree_symbol))
    else:
        sys.exit(2)
