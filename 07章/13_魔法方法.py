# 特殊方法 ：以 __xxx__ 命名的特殊方法（双下划线开头和结尾），也称为“魔术方法”（Magic Methods）。
# 特点
# 不需要手动调用，Python会在特定场景下自动调用这些方法。
# 用于实现类的特定行为，如运算符重载、对象初始化、字符串表示等。

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # __str__ 在顶级类 object 存在
    # 但是打印的并不是我们想要的 可以在Person上自己写 __str__ 方法
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# 创建对象时自动调用 __init__
p1 = Person("张三", 18, '男')
print(p1.name, p1.age)  # 张三 18
print(p1) # Person(name=张三, age=18)
print(str(p1))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print(f'self.x = {self.x}')
        print(f'self.y = {self.y}')
        print(f'other.x = {other.x}')
        print(f'other.y = {other.y}')
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print('v1= ', v1.__dict__)
print('v2= ', v2.__dict__)
v3 = v1 + v2  # 自动调用 __add__
print('v3= ', v3.__dict__)
# print(v3.x, v3.y)  # 输出：4 6


class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

ml = MyList([1, 2, 3, 4, 5])
print(len(ml))  # 自动调用 __len__，输出：5

# 特殊方法是Python中强大的特性，通过实现这些方法，可以让自定义类的行为更符合Python的内置语法和使用习惯，提升代码的可读性和易用性。
