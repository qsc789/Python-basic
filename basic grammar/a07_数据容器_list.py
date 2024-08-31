# 列表定义
name_list=["aaa","bbb","ccc"]
print(name_list)
print(type(name_list))
# 嵌套列表
my_list=[[1,2,3],[4,5,6]]
print(my_list)
print((type(my_list)))

my_list1=["aaa",11,True]# 元素类型不受限
print(my_list1)
print((type(my_list1)))

# 列表遍历
for name in name_list:
    print(name)
# 顺序
print(name_list[0])
print(name_list[1])
print(name_list[2])
# 逆序
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])
# 嵌套列表遍历
print(my_list[0][0])
print(my_list[0][1])
print(my_list[0][2])
print(my_list[1][-1])
print(my_list[1][-2])
print(my_list[1][-3])

# 列表操作
# 查询元素
print("aaa" in name_list)# 是否存在
print((name_list.index("aaa")))
# 修改元素
name_list[0]="AAA"
print(name_list)
name_list[0]="aaa"
# 插入元素
name_list.insert(1,"BBB")# 在索引1位置插入元素
print(name_list)# ['aaa', 'BBB', 'bbb', 'ccc']
# 追加元素到尾部
name_list.append("ddd")
print(name_list)
name_list.extend(["eee","fff"])
print(name_list)# ['aaa', 'BBB', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
# 删除元素
name_list.remove("BBB")# 删除第一个匹配的元素
print(name_list)
name_list.pop(5)# element=name_list.pop(5),可以接收
print(name_list)
del name_list[4]
print(name_list)
# 统计元素个数
print(f"\"aaa\"出现次数为:{name_list.count("aaa")}")
# 清空列表
name_list.clear()
print(name_list)

# 列表遍历
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j])
for item in my_list:
    for i in item:
        print(i)