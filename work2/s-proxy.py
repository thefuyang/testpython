# coding=utf-8
__author__ = 'YIN'
import urllib2
try:
    response = urllib2.urlopen('http://www.qiushibaike.com/')
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"
