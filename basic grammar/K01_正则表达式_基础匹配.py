import re

s="aaa bbb ccc aaa bbb ccc"
# match从头匹配
res=re.match("aaa",s)
print(res)
# search搜索整个字符串，找到第一个匹配的结果
res=re.search("bbb",s)
print(res)
# findall找到所有匹配结果
res=re.findall("ccc",s)
print(res)