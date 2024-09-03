class Student:
    name=None
    def say_hi(self):# 访问串成员变量必须加self
        print(f"hello,I am {self.name}")

    def say_hi2(self,msg):
        print(f"hello,I am {self.name},{msg}")

stu=Student()
stu.name="aaa"
stu.say_hi()

msg=input()
stu.say_hi2(msg)