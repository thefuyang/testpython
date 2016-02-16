# coding=utf-8
__author__ = 'YIN'
import re

pattern = re.compile(r'world')

match = re.search(pattern, 'hello world!')
if match is not None:
    print(match.group())
    print(match.groups())
    print(dir(match))
