# coding=utf-8
__author__ = 'YIN'
import cookielib
import urllib2
import urllib

filename = 'cookie.txt'
values = {"username": "admin", "password": "hisense"}
data = urllib.urlencode(values)

cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
url = 'http://localhost/guke/admin/php/login.php'
opener = urllib2.build_opener(handler)
response = opener.open(url, data)
print(response.read())
for item in cookie:
    print "Name = " + item.name
    print "Value = " + item.value
cookie.save(ignore_discard=True, ignore_expires=True)
