#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# Compute the average of a set of values entered by the user
# The running sum is printed as the numbers are entered

if __name__ == "__main__":
    sum_num = count = 0

    while True:
        try:
            num = int(input("Enter an integer (0 to quit): "))
        except ValueError:
            print("It is not an integer.")
            continue
        else:
            if num == 0:
                break

            count += 1
            sum_num += num
            print(f"The sum so far is {sum_num}")

    if count == 0:
        print("\nNo values were entered.")
    else:
        average = sum_num / count
        print(f"\nThe average is {average:.2f}")
