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
        password = ""
        for j in range(pdw_lengths[i]):

            random_index = random.randrange(len(alphabets))
            password = password + alphabets[random_index]

        password = mutate_capital(password)
        password = mutate_digits(password)
        password = mutate_symbols(password)

        passwords.append(password)

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
