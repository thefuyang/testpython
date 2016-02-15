# coding=utf-8
__author__ = 'YIN'
import urllib2
response = urllib2.urlopen("http://tieba.baidu.com")
print(response.read())

