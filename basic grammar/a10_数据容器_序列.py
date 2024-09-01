# 列表，元组，字符串都是序列
# 切片
my_list=[0,1,2,3,4,5,6]
res1=my_list[1:4]# 从1到4,前闭后开
print(res1)# [1, 2, 3]
res2=my_list[1:6:2]# 从1到6，步长为2
print(res2)# [1,3,5]

my_tuple=(0,1,2,3,4,5,6)
res3=my_tuple[1:4]# 从1到4,前闭后开
print(res3)# (1, 2, 3)
res4=my_tuple[1:6:2]
print(res4)# (1, 3, 5)

my_str="0123456"
res5=my_str[::-1]# 从头开始，最后结束，步长为-1,步长为负数表示从后向前取
print(res5)# "6543210"
res6=my_str[6:1:-1]
print(res6)# "65432"
res7=my_str[::-1][3:5]# 先倒序后切片
print(res7)# 32