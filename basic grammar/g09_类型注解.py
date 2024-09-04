# 基础数据类型注解
import json
from random import random# Alt+Enter快捷键
from typing import Union

var_1:int=10
var_2:str="aaa"
var_3:bool=True
# 类对象类型注解
class Student:
    pass
stu:Student=Student()
# 基础容器类型注解
my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_dict:dict={"name":"aaa"}
# 容器类型详细注解
my_list:list[int]=[1,2,3]
my_tuple:tuple[int,str,bool]=(1,"aaa",True)
my_dict:dict[str,int]={"name":123}
# 在注释中进行类型注解
var_1=random.randint(1,10)   # type:int
var_2=json.loads('{"name":"aaa"}')    # type:dict[str,str]
def func():
    return 10
var_3=func()      # type:int
# 类型注解只是备注，写错了也没事

# 函数形参类型注解
def add(x:int,y:int):
    return x+y
add(1,2)# 调用时Ctrl+p调出参数提示
# 对返回值类型注解
def func(data:list)->list:
    return data

# Union
my_list:list[Union[int,str]]=[1,2,"aaa"]
def func(data:Union[int,str])->Union[int,str]:
    pass