#!/usr/bin/env python3

""" The following program contains a function that validates a provided credit
card number using Luhn's algorithm. It then keeps asking the user for input,
and according to user decision either validates a provided number, a randomly
generated number or exits the program.
"""

import random
import sys
import re

# We define a function that takes a number and validates it using Luhn's
# algorithm. We will call it only once, but this way the code is better
# structured.

def luhn_val(val_number: int):
    val_list = [int(x) for x in str(val_number)]
    check_digit = val_list[-1]
    del val_list[-1]
    for i in range(len(val_list)):
        if i % 2 == 0:
            val_list[-(i + 1)] *= 2
            val_list[-(i + 1)] = sum(int(d) for d in str(val_list[-(i + 1)]))
    if 10 - sum(val_list) % 10 == check_digit: return True
    else: return False

# Next we create a regular expression - we're going to use it to make sure 
# the credit card number starts with the correct digit(s)

firstdig_regex = re.compile(r"^4|^5|^37|^6")

# The while loop encloses the actual program: asking for user input and
# validating it. We use True as condition so the program keeps asking for
# input until the user decides to exit.

while True:

    user_input = input("Please enter a credit card number to validate, "
                       + "enter 'e' to exit, "
                       + "or enter 'r' for a random number: \n")

    # The first if/else block decides on what the user wants to do:
    # exit the program, request a random number, or input their own.

    if not user_input: continue

    elif user_input in "Ee": sys.exit(0)

    elif user_input in "Rr":

        card_number = random.randint(1000000000000, 9999999999999999)

    else:
        try:
            card_number = int(user_input)
        except ValueError:
            print("Please provide ONLY a number or 'r' as input. \n")
            continue

    # The second if/else block validates the selected card number. It will tell
    # the user if the number is not the correct lenght, doesn't start with the 
    # right digits or if its invalid according to the Luhn algorithm.
    
    if not firstdig_regex.match(str(card_number)):
        print(f"{card_number} doesn't start with the correct digit(s), and "
              + "therefore is not a valid credit card number. \n")

    elif len(str(card_number)) > 16:
        print(f"{card_number} is too long, and therefore not a valid "
              + "credit card number. \n")

    elif len(str(card_number)) < 13:
        print(f"{card_number} is too short, and therefore not a valid "
              + "credit card number. \n")

    elif luhn_val(card_number):
        print(f"{card_number} is a valid credit card number. \n")

    else: print(f"{card_number} is not a valid credit card number. \n")