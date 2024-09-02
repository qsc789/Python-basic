# 捕获所有异常
try:
   f=open("D:/abc.txt","r",encoding="utf-8")
except:
    print("文件不存在，换模式")
    f = open("D:/abc.txt", "w", encoding="utf-8")

try:
    print(name)
except Exception as e:
    print(e)

try:
    print("123")
except Exception as e:
    print(e)
else:
    print("没有异常")

try:
    print(name)
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:# finally语句无论是否有异常都要执行
    print("必须执行这一条")

# 捕获特定异常
try:
    print(name)
except NameError as e:
    print("变量未定义")
    print(e)

# 捕获多个异常
try:
    1/0
except (NameError,ZeroDivisionError) as e:
    print(e)
