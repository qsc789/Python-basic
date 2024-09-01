my_str="abcdefg"
print(my_str.index('c'))
print(my_str.index("cde"))# 起始索引
# 替换
new_my_str=my_str.replace("cde","CDE")# 字符串不会被修改，需要一个新字符串接收替换后的字符串
print(new_my_str)
# 分割
my_list=my_str.split("d")# 按照"d"分割，返回一个列表
print(my_list)# ['abc', 'efg']
# 规整
my_str="  abc  def  ghi  cba  "
my_str=my_str.strip()# 去掉两端空格
print(my_str)# "abc  def  ghi  cba"
my_str=my_str.strip("abc")# 去掉字符串中所有'a','b',c'
print(my_str)# " def  ghi"
# 改变字符串必须有变量接收，原字符串不能直接改变

# 统计字符串出现次数
my_str="abcabcabcabc"
print(my_str.count("abc"))
print(my_str.count("a"))
# 长度
print(len(my_str))