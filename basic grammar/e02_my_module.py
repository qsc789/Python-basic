__all__=['func1']# all变量指定了import*时导入的函数
def func1(x,y):
    return x+y
def func2(x,y):
    return x*y
if __name__ == '__main__':# 用这种方式测试模块中的函数不会在导入时执行
    print(func1(1,2))