#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import re


class tieba:
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = seeLZ

    def getPage(self, pageNum):
        try:
            url = self.baseURL + '?see_lz=' + str(self.seeLZ) + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            print url
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败,原因%s", e.reason
                return None

if __name__=='__main__':
    baseURL = 'http://tieba.baidu.com/p/3442099352'
    tie = tieba(baseURL,1)
    tie.getPage(1)