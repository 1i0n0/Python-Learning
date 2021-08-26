#!/usr/bin/python3
# -*- coding: utf-8 -*-

def hello(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    try:
        name = input("What\'s your name?\n")
    except ValueError:
        print("Please enter a name.")
    else:
        hello(name)
