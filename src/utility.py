"""
Bunch of utilities for generating a strong password
"""

import random


def generate_password(pdw_lengths):

    """
    Function for generating initial password
    """

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for i in range(len(pdw_lengths)):
        buffer = ""
        for j in range(pdw_lengths[i]):

            random_index = random.randrange(len(alphabets))
            buffer = buffer + alphabets[random_index]

        buffer = mutate_capital(buffer)
        buffer = mutate_digits(buffer)
        buffer = mutate_symbols(buffer)

        passwords.append(buffer)

    return passwords


def mutate_digits(password):
    """
    Function for mutating the given password with random digits
    """
    return password


def mutate_symbols(password):
    """
    Function for mutating the given password with random symbols
    """
    return password


def mutate_capital(password):
    """
    Function for mutating the given password with capitalizing latters
    """
    return password
