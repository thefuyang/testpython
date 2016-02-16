# coding=utf-8
__author__ = 'YIN'
import re

pattern = re.compile(r'\d+')
str = 'insad123gjhg12hgjhg45jhg123hjg3jgh53jh4g1hgj3g4'
print(re.split(pattern, str))
print(re.findall(pattern, str))
for m in re.finditer(pattern, str):
    print m.group()
