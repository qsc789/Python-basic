# 装饰器的闭包写法
def outer(func):
    def inner():
        print("开始睡觉")
        func()
        print("起床")
    return inner


def sleep():
    import time
    import random
    print("睡眠中")
    time.sleep(random.randint(1,5))

fn=outer(sleep)
fn()

# 快捷写法
def outer(func):
    def inner():
        print("开始睡觉")
        func()
        print("起床")
    return inner

@outer
def sleep():
    import time
    import random
    print("睡眠中")
    time.sleep(random.randint(1,5))

sleep()# 给sleep增加功能

