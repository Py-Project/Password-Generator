'''
Author: Aditya Mangal 
Date:  17 september,2020
Purpose: python mini project

'''
from random import choice, shuffle
from string import (
    ascii_letters as letters,
    digits,
    punctuation,
)


if __name__ == "__main__":
    # collect input
    password_length = int(input("Enter the length of your password.\n"))

    # generate a sequence list
    character_sequence = [
        choice(letters + digits + punctuation) for _ in range(password_length)
    ]

    # shuffle the sequence list
    shuffle(character_sequence)

    # join the list into string
    pass_generated = "".join(character_sequence)

    # output the string
    print(f"Password generated!\nYour password is {pass_generated}")
