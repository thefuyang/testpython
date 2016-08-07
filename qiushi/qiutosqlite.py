#!/usr/bin/env python
# coding=utf-8
__author__ = 'YIN'
import urllib2
import urllib, time
import re
import sqlite3

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36Name'
host = 'www.qiushibaike.com'
headers = {'User-Agent': user_agent}

# def inserttosqlite(item):



try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    patternStr = r'''<h2>(.*?)</h2>.*?<div class="content.*?>(.*?)<!--(\d*?)-->.*?</div>(.*?)<div class="stats.*?<span class="stats-vote.*?class="number">(.*?)</i>'''
    pattern = re.compile(patternStr, re.S)
    items = re.findall(pattern, content)
    conn = sqlite3.connect('qiushu/qiu.db')
    for item in items:
        haveimg = re.search("img", item[3])
        ltime = time.localtime(int(item[2]))
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
        if not haveimg:
            print item[0], item[1], timeStr, item[4]

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
