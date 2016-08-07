#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import re

import datetime


class tieba:
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = seeLZ

    def getPage(self, pageNum):
        try:
            url = self.baseURL + '?see_lz=' + str(self.seeLZ) + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败,原因%s", e.reason
                return None

    def chuli(self, pageNum):
        content = self.getPage(pageNum).read().decode('utf-8')
        patternStr = r'''<h3.*?title="(.*?)"'''
        pattern = re.compile(patternStr, re.S)
        items = re.findall(pattern, content)
        nowdate = datetime.datetime.now()
        print("======%s======\n" % nowdate)
        for item in items:
            print(item)


if __name__ == '__main__':
    baseURL = 'http://tieba.baidu.com/p/3442099352'
    tie = tieba(baseURL, 1)
    tie.chuli(1)
