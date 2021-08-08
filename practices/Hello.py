#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def hello(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    try:
        name = input("What\'s your name?\n")
    except ValueError:
        print("Please enter a name.")
    else:
   2     hello(name)