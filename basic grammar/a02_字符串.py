name='aaa'
print(type(name))
name="bbb"
print(type(name))
name="""
ccc
"""
print(type(name))

# 字符串包含双引号
name='"ddd"'
print(name)
# 字符串内包含单引号
name="'eee'"
print(name)
# 使用\
name="\"fff\""
print(name)

# 字符串拼接
print("aaa"+"bbb")
name1="aaa"
name2="bbb"
print(name1+name2)

# 字符串格式化
name="aaa"
message="hello,%s"%name
print(message)
print(f"hello,{name}")

num1=100
num2=200
message="num1=%s,num2=%s"%(num1,num2)# 或者message="num1=%d,num2=%d"%(num1,num2)
print(message)

# 精度控制
num1=3.1415926
message="num1=%.2f"%num1
print(message)

num1=11
num2=11.345
print("%5d"%num1)# 左对齐，宽度为5
print("%7.2f"%num2)
print("%.2f"%num2)
