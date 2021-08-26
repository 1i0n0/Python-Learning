#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Compute the average of a list of values entered by the user

def _average(arr):
    num_count = len(arr)
    if count == 0:
        return None
    else:
        return sum(arr) / num_count


if __name__ == "__main__":
    sum_num = count = 0
    array = []

    while True:
        try:
            num = int(input("Enter an integer (0 to quit): "))
        except ValueError:
            print("It is not an integer.")
            continue
        else:
            if num == 0:
                break
            else:
                array.append(num)

    average = _average(array)
    if not average:
        print("\nNo values were entered.")
    else:
        print(f"\nThe average is {average:.2f}")
