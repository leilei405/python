# 定义父类
class Animal:
    pass

# 定义子类（继承自 Animal）
class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 定义无关类
class Car:
    pass

# 创建实例
dog_instance = Dog()
cat_instance = Cat()
car_instance = Car()

# isinstance() 函数
# 作用 ：判断某个对象是否为指定类或其子类的实例。
# 语法 ： isinstance(instance, Class)
# 返回值 ：布尔值（ True 或 False ）。

# 使用 isinstance 判断实例类型
print("判断 dog_instance 是否是 Dog 的实例:", isinstance(dog_instance, Dog))  # True
print("判断 dog_instance 是否是 Animal 的实例:", isinstance(dog_instance, Animal))  # True（子类实例也是父类的实例）
print("判断 cat_instance 是否是 Dog 的实例:", isinstance(cat_instance, Dog))  # False
print("判断 car_instance 是否是 Animal 的实例:", isinstance(car_instance, Animal))  # False

# issubclass() 函数
# 作用 ：判断某个类是否是另一个类的子类。
# 语法 ： issubclass(Class1, Class2)
# 返回值 ：布尔值（ True 或 False ）。

# 使用 issubclass 判断类的继承关系
print("判断 Dog 是否是 Animal 的子类:", issubclass(Dog, Animal))  # True
print("判断 Cat 是否是 Animal 的子类:", issubclass(Cat, Animal))  # True
print("判断 Animal 是否是 Dog 的子类:", issubclass(Animal, Dog))  # False
print("判断 Car 是否是 Animal 的子类:", issubclass(Car, Animal))  # False

