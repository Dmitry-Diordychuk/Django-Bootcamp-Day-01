#!/usr/bin/python3
# coding: utf-8


def print_numbers():
    """
    Print numbers.txt
    """
    path = "numbers.txt"
    file = open(path, 'r')
    numbers = file.readline().split(',')
    numbers[-1] = numbers[-1].replace('\n', '')
    print(*numbers, sep='\n')
    file.close()


if __name__ == '__main__':
    print_numbers()
