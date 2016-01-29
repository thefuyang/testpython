#!/usr/bin/env python
# coding=utf-8


def plusplus(a, b):
    return a * b


def prod(x):
    return reduce(plusplus, x)


if __name__ == '__main__':
    print sum([1, 3, 2, 4, 5, 2, 3, 4, 5, 33, 1])
    print plusplus(11, 2)
    print reduce(plusplus, [11, 2, 3, 11])
    print prod([11, 2, 3, 4])
