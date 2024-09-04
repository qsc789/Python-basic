class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

    def __lt__(self,other):# 用于大小比较（不包含等于
        return self.age<other.age

    def __le__(self,other):# 大小比较，包含等号
        return self.age<=other.age

    def __eq__(self,other):# 用于比较是否相等
        return self.age==other.age

stu1=Student("aaa",18)
stu2=Student("bbb",30)
print(str(stu1))
print(stu1<stu2)
print(stu1<=stu2)
print(stu1==stu2)