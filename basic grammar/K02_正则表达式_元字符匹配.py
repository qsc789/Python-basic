import re

s="1727%&^ &^@!6712fvwdjyvy ()*^H [1,2,3,4,5] 63167"

# .匹配任1字符，\n除外，\.匹配.本身
# []匹配[]中的字符
# \d 匹配数字,r表示反斜杠无效
# \D匹配非数字
# \s匹配空格，tab
# \S匹配非空白
# \w匹配字母和数字和_
# \W匹配非字母和数字
res=re.findall(r'\d',s)
print(res)
res=re.findall(r'[a-zA-Z]',s)# []中是范围
print(res)

# 太复杂了，用的时候再学吧

