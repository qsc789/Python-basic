def func(compute):
    return compute(2,3)
def compute(x,y):
    return x+y

print(func(compute))
print(func(lambda x,y:x+y))# lambda匿名函数，没有函数名，函数体只有一行