my_set={0,1,2,3,4,5,5}
print(my_set)# {0,1,2,3,4,5},去重
# 添加
my_set={0,1,2,3,4,5}
my_set.add(6)
print(my_set)# {0, 1, 2, 3, 4, 5, 6}
# 移除元素
my_set.remove(6)
print(my_set)# {0, 1, 2, 3, 4, 5}
# 随机取出一个元素
element=my_set.pop()
print(element)
print(my_set)
# 清空
my_set.clear()
print(my_set)# set(),表示空集合
# 曲两个集合的差集
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3=set1.difference(set2)# {1, 2, 3}
print(set3)
set4=set2.difference(set1)# {8, 6, 7}
print(set4)
# 消除差集,删除一样的部分
set1.difference_update(set2)
print(set1)# {1, 2, 3}
# 合并集合
set3=set1.union(set2)
print(set3)# {1, 2, 3, 4, 5, 6, 7, 8}
# 统计集合元素数量
print(len(set3))
# 集合遍历
for i in set3:
    print(i)