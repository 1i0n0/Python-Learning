#!/usr/bin/python3
# -*- coding = UTF-8 -*-

def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if(num % i) == 0:
                return False
        return True


if __name__ == "__main__":
    number = int(input("Enter a number: \n"))

    if is_prime(number):
        print(f"{number} IS a prime number.")
    else:
        print(f"{number} IS NOT a prime number.")
