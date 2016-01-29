#!/usr/bin/env python
# coding=utf-8


def noprim(x):
    if x == 1:
        return x
    else:
        for i in range(2, x):
            if x % i is 0:
                return x

if __name__ == '__main__':
    a = filter(noprim, range(1, 101))
    print a
