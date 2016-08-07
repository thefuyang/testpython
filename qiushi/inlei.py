#!/usr/bin/env python
# coding=utf-8
__author__ = 'YIN'
import urllib2
import urllib
import re
import thread
import Tools


class Qsbk:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36Name'
        self.headers = {'User-Agent': self.user_agent}
        self.url = 'http://www.qiushibaike.com/hot/page/'
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = self.url + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"链接糗百失败，错误原因：", e.reason
                return None

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print u"页面加载失败"
            return None
        patternStr3 = r'''<h2>(.*?)</h2>.*?<div class="content.*?>(.*?)<!--(\d*?)-->.*?</div>(.*?)<div class="stats.*?<span class="stats-vote.*?class="number">(.*?)</i>'''
        pattern = re.compile(patternStr3, re.S)
        items = re.findall(pattern, pageCode)
        nowpagestories = []
        for item in items:
            haveimg = re.search("img", item[3])
            if not haveimg:
                nowpagestories.append([item[0].strip(), Tools.cookstring(item[1]).strip(),
                                       Tools.changetime(item[2]).strip(), item[4].strip()])
        return nowpagestories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories is not None:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" % (page, story[0], story[2], story[3], story[1])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                pageStories = self.stories[0]
                # 当前读到的页数加一
                nowPage += 1
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.getOneStory(pageStories, nowPage)

if __name__ == '__main__':
    spider = Qsbk()
    spider.start()
