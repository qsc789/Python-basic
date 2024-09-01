my_dict={1:'a',
         2:'b',
         3:'c',
         4:'d',
         5:'e'}# key不能重复
print(my_dict)
print(my_dict[1])
new_dict={"A":
              {1:"b",2:"c",3:"d"}}
print(new_dict)
print(new_dict["A"])
print(new_dict["A"][2])
# 字典操作
# 新增元素
my_dict[6]='f'
# 删除元素
my_dict.pop(1)# 同时也有返回值
print(my_dict)
# 获取全部key
print(my_dict.keys())
# 遍历
for key in my_dict:
    print(key,my_dict[key])
# 统计元素数量
print(len(my_dict))