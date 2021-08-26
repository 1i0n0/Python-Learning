#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fathoms2feet(fathoms):
    return 6 * fathoms


if __name__ == "__main__":
    try:
        fathoms = int(input("Fathom(s): "))
    except ValueError:
        print("Please enter an integer.")
    else:
        print("There are {0} feet in {1} fathom(s).".format(fathoms2feet(fathoms), fathoms))
