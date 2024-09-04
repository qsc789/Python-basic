class Phone:
    IMEI=None
    producer="aaa"

    def call_by_5g(self):
        print("5g通话")

class MyPhone(Phone):
    producer = "bbb"# 复写属性

    def call_by_5g(self):# 复写方法
        print("开启CPU单核模式，省电")
        print("5g通话")
        print("关闭CPU单核模式")
        # 调用父类方法
        Phone.call_by_5g(self)# 加self
        super().call_by_5g()# 不加self
        print(f"父类的厂商为{super().producer}")

phone=MyPhone()
phone.call_by_5g()
print(phone.producer)
# 调用父类成员属性的方法
print(f"父类的厂商为{Phone.producer}")
