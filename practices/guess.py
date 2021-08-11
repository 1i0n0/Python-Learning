#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# Play a simple guessing game with the user

import random

if __name__ == "__main__":
    max_num = 10

    print(f"I'm thinking of a number between 1 and {max_num}.")
    answer = random.randrange(1, max_num)

    while True:
        try:
            guess = int(input("Guess what it is: "))
        except ValueError:
            print("This is not a number. Please try again or enter 0 to exit.")
            continue
        else:
            if guess == 0:
                print(f"The number was {answer}.")
                break
            elif guess == answer:
                print("You got it! Good guessing!")
                break
            else:
                print("Sorry, that is not correct. Please try again or enter 0 to exit.")
                continue
    
