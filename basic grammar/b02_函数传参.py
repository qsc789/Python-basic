def user_info(*args):# 接收无限参数
    print(args)

user_info(1,2,3)# 以元组形式打印
user_info(4,5,6,7,8)

def user_info2(**kwargs):# 限制键值对形式
    print(kwargs)

user_info2(name="aaa",age=18)