# 闭包无需定义全局变量，而是可以访问的外部变量
def outer(logo):
    def inner(msg):# 内部变量依赖外部变量logo
        print(f"<{logo}>{msg}<{logo}>")

    return inner# 返回的是inner函数

fn1=outer("aaa")# 此时fn1是inner函数
fn1("hello")
fn1("hi")

# 使用nonlocal关键字修改外部变量的值
def outer(num1):
    def inner(num2):
        nonlocal num1# 访问外部变量需要nonlocal修饰
        num1+=num2
        print(num1)
    return inner

fn=outer(10)
fn(10)