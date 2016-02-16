# coding=utf-8
__author__ = 'YIN'
import re


def prn_obj(obj):
    print ', '.join(['%s:%s' % item for item in obj.__dict__.items()])


parttern = re.compile(r'hello')

result1 = re.match(parttern, 'hello')
result2 = re.match(parttern, 'helloO CQC!')
result3 = re.match(parttern, 'helo CQC!')
result4 = re.match(parttern, 'hello CQC!')
m = re.match(r'(?P<word>\w+) (\w+)(?P<sign>.*)', 'hello world!')
# 如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！'


# 如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print result2.group()
else:
    print '2匹配失败！'


# 如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print result3.group()
else:
    print '3匹配失败！'

# 如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print result4.group()
else:
    print '4匹配失败！'

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print "m.span(3):", m.span(3)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')
