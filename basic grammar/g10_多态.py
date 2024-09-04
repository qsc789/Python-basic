class Animal:# 含有抽象方法的类是抽象类，空实现的方法是抽象方法
    def speak(self):
        pass# 让父类确定有哪些方法，具体方法让子类实现

class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_sound(animal:Animal):# 需要传入父类对象
    animal.speak()

dog=Dog()
cat=Cat()
make_sound(dog)
make_sound(cat)
