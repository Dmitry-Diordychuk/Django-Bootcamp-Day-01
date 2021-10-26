#!/usr/bin/python3
# coding: utf-8


import sys

def get_capital(state):
    """
    Find out capital of the state.
    :param state: state which capital is searching.
    """
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    postal_code = states.get(state)
    return capital_cities.get(postal_code)


def run_program():
    """
    Check sys.argv len and print state capital, error message or nothing.
    :return: None
    """
    if len(sys.argv) != 2:
        return
    capital = get_capital(sys.argv[1])
    if capital:
        print(capital)
    else:
        print("Unknown state")


if __name__ == '__main__':
    run_program()
