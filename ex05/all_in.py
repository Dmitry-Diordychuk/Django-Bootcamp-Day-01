#!/usr/bin/python3
# coding: utf-8


import sys


def get_data():
    """
    Get dictionaries
    :return: states dictionary and cities dictionary
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
    return states, capital_cities


def get_capital(state):
    """
    Find out capital of the state.
    :param state: state which capital is searching.
    """
    states, capital_cities = get_data()
    postal_code = states.get(state)
    return capital_cities.get(postal_code)


def get_state(capital):
    """
    Find out capital of the state.
    :param capital: capital which state is searching.
    """
    states, capital_cities = get_data()
    capital_cities = dict([el[::-1] for el in capital_cities.items()])
    postal_code = capital_cities.get(capital)
    states = dict([el[::-1] for el in states.items()])
    return states.get(postal_code)


def run_program():
    """
    Check sys.argv len and print states of capital cities, capital cities of states, error message or nothing.
    :return: None
    """
    if len(sys.argv) != 2:
        return
    expressions = sys.argv[1].split(',')

    expressions = [ex.strip() for ex in expressions if ex.strip() != ""]

    for ex in expressions:
        state = get_state(ex.title())
        city = get_capital(ex.title())
        if state:
            print(ex.title(), "is the capital of", state)
        elif city:
            print(city, "is the capital of", ex.title())
        else:
            print(ex, "is neither a capital city nor a state")


if __name__ == '__main__':
    run_program()
