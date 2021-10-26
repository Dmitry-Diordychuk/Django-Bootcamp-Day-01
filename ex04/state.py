#!/usr/bin/python3
# coding: utf-8


import sys


def get_state(capital):
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
    capital_cities = dict([el[::-1] for el in capital_cities.items()])
    postal_code = capital_cities.get(capital)
    states = dict([el[::-1] for el in states.items()])
    return states.get(postal_code)


def run_program():
    """
    Check sys.argv len and print state of capital city, error message or nothing.
    :return: None
    """
    if len(sys.argv) != 2:
        return
    state = get_state(sys.argv[1])
    if state:
        print(state)
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    run_program()
