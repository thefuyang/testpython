# coding=utf-8
__author__ = 'YIN'
import urllib
import urllib2
values = {"username": "admin", "password": "111"}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36Name',
           'Refer': 'http://tieba.baidu.com',
           'Host': 'www.qiushibaike.com'}
data = urllib.urlencode(values)
url = "http://www.qiushibaike.com"
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
print(response.read())
