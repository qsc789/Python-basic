age=30
if age>=18:
    print("成年")

age=int(input("输入年龄："))
if age>=18:
    print("成年")
else:
    print("未成年")

height=int(input("输入身高（cm）："))
vip_level=int(input(("输入vip等级（1-5）：")))
if height<=120:
    print("免费")
elif vip_level>=3:
    print("免费")
else:
    print("收费")