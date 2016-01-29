#!/usr/bin/env python
# coding=utf-8


def odd(x):
    n, a, b = 0, 0, 1
    while n < x:
        yield b
        a, b = b, a + b
        n += 1


def change(name):
    if isinstance(name, str) is not None:
        return name.title()


if __name__ == '__main__':
    for x in odd(10):
        print x
    L = map(change, ['adam', 'LISA', 'barT'])
    print L


