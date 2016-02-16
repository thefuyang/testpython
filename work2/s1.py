# coding=utf-8
__author__ = 'YIN'
import urllib2
response = urllib2.urlopen('http://www.qiushibaike.com')
print(response.read())

