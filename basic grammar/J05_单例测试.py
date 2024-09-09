from J04_str_tools import str_tools
s1=str_tools
s2=str_tools
print(id(s1))# id相同，说明是单例
print(id(s2))
# 单例模式可以节省内存，节省创建对象的开销