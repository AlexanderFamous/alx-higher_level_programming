#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        mul = -1
        number *= -1
    result = number % 10
    print(result, end="")
    return (result)
