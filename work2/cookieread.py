# coding=utf-8
__author__ = 'YIN'
import cookielib
import urllib2

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', True, True)
req = urllib2.Request("http://localhost/guke/admin/php/manage.php")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
