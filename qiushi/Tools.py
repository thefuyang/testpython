# coding=utf-8
__author__ = 'YIN'
import time
import re

def changetime(xtime):
    ltime = time.localtime(int(xtime))
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
    return timeStr


def cookstring(xstr):
    replace_br = re.compile('<br\s*/>')
    return re.sub(replace_br, "\n", xstr)
