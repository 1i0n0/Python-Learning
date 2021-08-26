#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Test a string to see if it is a palindrome
def is_palindrome(s):
    s.strip()
    left = 0
    right = len(s) - 1

    while s[left] == s[right] and left < right:
        left += 1
        right -= 1

    if left < right:
        return False
    else:
        return True


if __name__ == "__main__":
    _str = input("Enter a potential palindrome: ")
    if is_palindrome(_str):
        print("That string IS a palindrome.")
    else:
        print("That string IS NOT a palindrome.")
