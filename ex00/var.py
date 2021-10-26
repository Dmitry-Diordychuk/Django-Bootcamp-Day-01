#!/usr/bin/python3
# coding: utf-8


def my_var():
    """
    Prints variables type
    """
    number = 42
    print(number, "has a type", type(number))
    number_str = "42"
    print(number_str, "has a type", type(number_str))
    my_string = "quarante-deux"
    print(my_string, "has a type", type(my_string))
    float_number = 42.0
    print(float_number, "has a type", type(float_number))
    is_boolean = True
    print(is_boolean, "has a type", type(is_boolean))
    my_list = [42]
    print(my_list, "has a type", type(my_list))
    my_dict = {42: 42}
    print(my_dict, "has a type", type(my_dict))
    my_tuple = (42, )
    print(my_tuple, "has a type", type(my_tuple))
    my_set = set()
    print(my_set, "has a type", type(my_set))


if __name__ == '__main__':
    my_var()
