# 定义父类
class Animal:
    def make_sound(self):
        print("动物发出叫声")

# 定义子类1：狗
class Dog(Animal):
    def make_sound(self):  # 重写父类方法
        print("汪汪汪！")

# 定义子类2：猫
class Cat(Animal):
    def make_sound(self):  # 重写父类方法
        print("喵喵喵！")

# 测试函数：接收 Animal 类型的参数
def animal_sound(animal: Animal):  # 类型注解
    animal.make_sound()  # 调用方法时，根据实际对象类型执行不同实现

# 测试
dog = Dog()
cat = Cat()
animal_sound(dog)  # 输出：汪汪汪！
animal_sound(cat)  # 输出：喵喵喵！