#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# Print the multiples of 7 and the numbers contain 7
# up to a user-specified limit

if __name__ == "__main__":
    _max = int(input("Enter an upper limit: "))
    count = 0

    for num in range(1, _max + 1):
        if num % 7 == 0 or str(num).find('7') >= 0:
            print(f"{num}\t", end='')
            count += 1

        # 5 numbers per line
        if count != 0 and count % 5 == 0:
            print()
            count = 0
